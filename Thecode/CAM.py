import cv2
from deepface import DeepFace
import tkinter as tk


def initialize_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    return cap


def detect_faces(frame, face_cascade):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces


def analyze_face(face, action):
    results = DeepFace.analyze(face, actions=[action], enforce_detection=False)
    if action == 'emotion' or action == 'gender':
        # Extract the dictionary from the list
        result_dict = results[0][action]
        # Find the key with the maximum value
        dominant = max(result_dict.items(), key=lambda x: x[1])[0]
        return dominant
    else:
        return results[0][action]


def draw_emotions(frame, faces, action):
    font = cv2.FONT_HERSHEY_SIMPLEX
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face = frame[y:y + h, x:x + w]
        emotions = analyze_face(face, action)
        print(type(emotions), emotions)
        if isinstance(emotions, int):
            emotion_str = str(emotions)
            cv2.putText(frame, emotion_str, (x, y + h + 20), font, 1, (0, 0, 255), 2, cv2.LINE_4)
        else:
            for i, emotion in enumerate(emotions):
                emotion_str = str(emotion)
                cv2.putText(frame, emotion_str, (x + i*50, y + h + 20), font, 1, (0, 0, 255), 2, cv2.LINE_4)
    return frame


def main():
    print("Starting webcam...")
    cap = initialize_webcam()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print("Entering main loop...")

    root = tk.Tk()
    action = tk.StringVar(root)
    action.set('emotion')

    emotion_button = tk.Radiobutton(root, text="Emotion", variable=action, value='emotion')
    age_button = tk.Radiobutton(root, text="Age", variable=action, value='age')
    gender_button = tk.Radiobutton(root, text="Gender", variable=action, value='gender')
    emotion_button.pack()
    age_button.pack()
    gender_button.pack()

    while True:
        ret, frame = cap.read()
        faces = detect_faces(frame, face_cascade)
        frame = draw_emotions(frame, faces, action.get())  # use the get method to get the action
        cv2.imshow('My Emotion Detection Project', frame)
        key = cv2.waitKey(2) & 0xFF
        if key == ord('q'):
            break
        root.update()

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
