# Real-Time-Object-and-Face-Detection
A real-time object and face detection system built using Python, OpenCV, and YOLOv8. Uses a webcam to detect and visualize objects and human faces with bounding boxes.

# Real-Time Object and Face Detection

A real-time object and face detection project built using **Python, OpenCV, and YOLOv8**. The application uses a webcam to detect objects and human faces, displaying detection results with bounding boxes in real time.

## Features

- Real-time webcam video capture.
- General object detection using YOLOv8.
- Face detection using a YOLO-based face detection model.
- Bounding boxes and detection labels.
- Live detection window using OpenCV.
- Press `X` to exit the application.

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLOv8
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Real-Time-Object-and-Face-Detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Real-Time-Object-and-Face-Detection
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the required model weights:
   - `yolov8n.pt`
   - `yolov8m-face.pt`

   Place both model files in the project directory. The face detection model must be compatible with Ultralytics YOLO.

## Usage

Run the Python script:

```bash
python faces.py
```

Make sure your webcam is connected and accessible.

Press `X` to close the detection window.

## Project Structure

```text
Real-Time-Object-and-Face-Detection/
│
├── faces.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

- Real-time object tracking.
- FPS counter for performance monitoring.
- Improved detection accuracy.
- Support for additional YOLO models.

## License

This project is intended for educational and learning purposes.
