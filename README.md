# 🚆 Railway Loco Pilot Identity Verification System

A real-time face verification system developed as part of an **Indian Railways Internship** to verify the identity of railway loco pilots before train operation.

The system ensures that the **same authorized pilot who passed the alcohol test** is operating the train.

---

## 📌 Problem Statement

Manual identity verification of railway loco pilots is time-consuming and prone to human error.  
This project automates the verification process by matching a **real-time camera image** with a **stored driver image**, improving safety and operational efficiency.

---

## 🎯 Project Objectives

- Verify the identity of loco pilots using facial recognition
- Match real-time camera input with stored database images
- Prevent unauthorized personnel from operating trains
- Reduce manual verification time
- Improve safety compliance

---

## 🧠 System Overview

1. A reference image of the authorized driver is stored in the system  
2. A live camera captures the driver’s face in real time  
3. The detected face is compared with the stored image  
4. A verification decision is made:
   - ✅ Driver Verified
   - ❌ Unauthorized Person

---

## 🏗️ System Architecture

Stored Driver Image
↓
Face Detection
↓
Feature Extraction
↓
Identity Matching
↓
Verification Decision


---

## ⚙️ Technologies Used

- Python 3
- OpenCV (Haar Cascade + LBPH Face Recognizer)
- NumPy

---

## 🧪 Verification Logic

- Face detection using Haar Cascades
- Feature extraction using LBPH
- Confidence-based identity matching
- Face-size based gating to reject overly close faces
- Real-time verification decision

---

## ▶️ How to Run

```bash
git clone https://github.com/<your-username>/railway-loco-pilot-face-verification.git
cd railway-loco-pilot-face-verification

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python src/camera_test.py

Expected Output

| Scenario                              | Output              |
| ------------------------------------- | ------------------- |
| Authorized driver (normal distance)   | Driver Verified     |
| Authorized driver (too close)         | Move Back           |
| Unauthorized person (normal distance) | Unauthorized Person |
| Unauthorized person (too close)       | Move Back           |


Limitations

Works best in controlled environments

Requires frontal face images

No liveness detection implemented

Single-camera setup


Future Enhancements

Multi-frame verification

Liveness detection (blink / head movement)

Deep learning-based face embeddings

Multi-camera support

Integration with alcohol detection hardware


Author

Arushi
Indian Railways Internship
Face Verification Module




