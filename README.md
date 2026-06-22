Railway Loco Pilot Face Verification System

Overview

This project implements a real-time face verification system developed as part of an Indian Railways Internship.
The purpose of the system is to verify the identity of a railway loco pilot before commencement of train operations by matching a live camera image with a stored reference image.

The system ensures that only the authorized loco pilot, who has completed mandatory safety checks such as alcohol testing handled externally, is allowed to operate the train.

This repository focuses only on the face verification module. The alcohol detection system is considered an external hardware component.

---

Problem Statement

Manual identity verification of loco pilots before train operation is time-consuming, prone to human error, and difficult to scale across large railway networks.

An automated face verification mechanism is required to ensure accurate and fast identity verification, thereby improving operational efficiency and safety compliance.

---

Project Objectives

* Verify the identity of railway loco pilots using facial recognition
* Match real-time camera input with stored driver images
* Prevent unauthorized personnel from operating trains
* Reduce manual verification time
* Improve overall railway safety compliance

---

System Overview

The system captures a live video feed of the loco pilot and compares the detected face with a stored reference image.

The verification decision is displayed in real time as:

* Driver Verified
* Unauthorized Person
* Move Back (when the face is too close to the camera)

---

System Architecture

Live Camera Feed
↓
Face Detection using Haar Cascade
↓
Feature Extraction using LBPH
↓
Similarity Comparison
↓
Verification Decision

---

Technology Stack

* Programming language: Python 3
* Computer vision library: OpenCV
* Face recognition method: LBPH (Local Binary Pattern Histogram)
* Numerical processing: NumPy
* Platform: Windows
* Version control: Git and GitHub

---

Project Structure

railway-loco-pilot-face-verification
│
├── src
│   └── face_verification.py
│
├── data
│   └── known_faces
│       └── driver_001.jpg
│
├── results
│
├── README.md
├── requirements.txt
├── future_scope.md
└── .gitignore

---

How the System Works

1. A reference image of the authorized loco pilot is stored in the system
2. A live image is captured using a front-facing camera
3. The face is detected using a Haar Cascade classifier
4. Facial features are extracted using the LBPH algorithm
5. Extracted features are compared with the stored reference image
6. A verification decision is displayed on the screen

---

How to Run the Project

1. Clone the repository from GitHub
2. Install the required dependencies
3. Add the authorized pilot’s image to the known_faces folder
4. Run the face verification script
5. Press ESC to exit the camera window

---

Expected Output

* Authorized pilot at normal distance: Driver Verified
* Authorized pilot too close to camera: Move Back
* Unauthorized person at normal distance: Unauthorized Person
* Unauthorized person too close to camera: Move Back

Results and Screenshots

The following screenshots demonstrate the working of the face verification system under different conditions.

Authorized pilot verification:
results/verified_face.png

Unauthorized person detection:
results/unknown_face.png

No face detected case:
results/no_face_detected.png


---

Key Design Decisions

* Face-size based gating is used to reject faces that are too close to the camera
* Verification is performed only under controlled distance conditions
* Lightweight algorithms are used to ensure real-time performance inside locomotive cabins

---

Limitations

* Accuracy decreases under poor lighting conditions
* Requires frontal face images
* Designed for single-person verification
* Liveness detection is not implemented
* Optimized for controlled indoor environments

---

Future Enhancements

* Multi-frame verification for improved accuracy
* Liveness detection using eye blink or head movement
* Deep learning based face recognition models such as FaceNet or ArcFace
* Multi-camera setup with front and side views
* Integration with alcohol detection hardware
* Deployment on embedded edge devices

---


