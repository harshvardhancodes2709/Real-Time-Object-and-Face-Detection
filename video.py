
import cv2
from ultralytics import YOLO

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load YOLO models
model = YOLO("yolov8n.pt")
face_model = YOLO("yolov8m-face.pt")

# Create window once
cv2.namedWindow("My Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("My Window", 900, 650)
cv2.moveWindow("My Window", 200, 100)

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        print("Could not access webcam.")
        break

    # Detect objects/persons
    result = model(frame, verbose=False)

    # Draw object detection results
    cat_person = result[0].plot()

    # Detect faces
    face_result = face_model(frame, verbose=False)

    # Draw face detection results over the existing frame
    cat_person_face = face_result[0].plot(img=cat_person)

    # Display webcam feed
    cv2.imshow("My Window", cat_person_face)

    # Press X to exit
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()
