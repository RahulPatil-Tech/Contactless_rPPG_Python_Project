import cv2
import numpy as np
import pandas as pd

def detect_face(frame):
    face_cascade = cv2.CascadeClassifier('Contactless rPPG Python/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    return faces

def calculate_hr(frame, face):  # Pass 'frame' as an argument here
    (x, y, w, h) = face
    roi = frame[y:y+h, x:x+w]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    hr = 60 * len(contours) / 60
    return hr

def calculate_rr(frame, face):  # Pass 'frame' as an argument here
    (x, y, w, h) = face
    roi = frame[y:y+h, x:x+w]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    rolling_sum = np.cumsum(gray)
    rr = len(rolling_sum[rolling_sum > 0]) / 60
    return rr

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        faces = detect_face(frame)

        for face in faces:
            hr = calculate_hr(frame, face)  # Pass 'frame' to the functions
            rr = calculate_rr(frame, face)  # Pass 'frame' to the functions

            (x, y, w, h) = face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a blue rectangle around the face

            # Display heart rate and respiratory rate on the frame
            cv2.putText(frame, f"Heart rate: {hr:.2f}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.putText(frame, f"Respiratory rate: {rr:.2f}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            # Display a constant number on the frame
            constant_number = 42  # Change this to the desired constant number
            cv2.putText(frame, f"Constant: {constant_number}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            df = pd.DataFrame({"Heart rate": [hr], "Respiratory rate": [rr]})
            df.to_csv("data.csv")

        cv2.imshow('frame', frame)
        
        key = cv2.waitKey(1)
        if key == ord('Q') or key == ord('q'):  # Quit if 'Q' or 'q' is pressed
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()