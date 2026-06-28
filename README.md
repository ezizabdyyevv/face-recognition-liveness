# Face Recognition + Liveness Detection

Real-time face recognition system with liveness detection using DeepFace and OpenCV.

## Features
- 👁️ Liveness detection (blink-based anti-spoofing)
- 🧠 Real-time face recognition using DeepFace
- 📷 Webcam-based pipeline
- 🚫 Rejects photo/screen attacks

## Tech Stack
- Python 3.13
- OpenCV
- DeepFace
- Haar Cascade Classifier

## How it works
1. Camera opens and asks user to blink 3 times (liveness check)
2. Once liveness is confirmed, face recognition starts
3. If the face matches someone in the database → shows their name
4. If unknown → shows "Bilinmiyor"

## Setup

```bash
# Clone the repo
git clone https://github.com/ezizabdyyevv/face-recognition-liveness.git
cd face-recognition-liveness

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install deepface opencv-python

# Add your photos to database folder
mkdir database/YourName
# Put 3-5 photos of yourself in that folder

# Run
python main.py
```

## Project Structure
face-recognition-liveness/

├── database/          # Known faces

├── main.py            # Main application

└── README.md