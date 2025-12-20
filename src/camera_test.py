import cv2
import os
import numpy as np

# -----------------------------
# Paths and setup
# -----------------------------
KNOWN_FACES_DIR = "known_faces"
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

# -----------------------------
# Prepare training data
# -----------------------------
faces = []
labels = []
current_label = 0

for file in os.listdir(KNOWN_FACES_DIR):
    if file.lower().endswith((".jpg", ".png")):
        img_path = os.path.join(KNOWN_FACES_DIR, file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        detected = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in detected:
            faces.append(img[y:y+h, x:x+w])
            labels.append(current_label)
            current_label += 1
            break

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))

print("Driver image loaded. Camera starting...")

# -----------------------------
# Start camera
# -----------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected = face_cascade.detectMultiScale(gray, 1.3, 5)

    frame_height, frame_width = frame.shape[:2]
    frame_area = frame_height * frame_width

    for (x, y, w, h) in detected:

        face_area = w * h

        # 🚫 Reject faces that are too close
        if face_area > 0.25 * frame_area:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(
                frame,
                "Move Back",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )
            continue

        face = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face)

        if confidence < 60:
            text = "Driver Verified"
            color = (0, 255, 0)
        else:
            text = "Unauthorized Person"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(
            frame,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow("Railway Loco Pilot Verification", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
