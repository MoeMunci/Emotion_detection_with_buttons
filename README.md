# README.md
# Emotion Detection with Buttons

This project is a webcam-based emotion, age, and gender detection tool using OpenCV, DeepFace, and Tkinter for a simple GUI. Users can select which attribute to detect (emotion, age, or gender) using radio buttons.

## Features

- Real-time face detection using OpenCV.
- Emotion, age, and gender analysis using DeepFace.
- Simple GUI for attribute selection with Tkinter.
- Results are displayed on the webcam feed.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- DeepFace
- Tkinter (usually included with Python)
- A working webcam

## Installation

1. Clone this repository or copy the code.
2. Install dependencies:
    ```sh
    pip install opencv-python deepface
    ```

## Usage

Run the main script:

```sh
python Thecode/CAM.py
```

- A window will open with radio buttons to select Emotion, Age, or Gender.
- The webcam feed will display detected faces and the selected attribute.
- Press `q` to quit.

## File Structure

- `Thecode/CAM.py` — Main script for webcam detection and GUI.

## Notes

- Make sure your webcam is connected.
- The first time you run DeepFace, it may download some models.

## License

This project is for educational purposes.