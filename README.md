# Real-Time AR Cube Projection with ArUco Markers

This project implements a real-time **Augmented Reality (AR)** system that detects **ArUco markers** from a webcam feed and projects a virtual **3D cube** onto each detected marker.  
It manually handles camera calibration, pose estimation, and 3D projection using **OpenCV** and **NumPy**, providing a deeper understanding of AR without a 3D game engine.

---

## Built With

- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/) (`opencv-python`)
- [NumPy](https://numpy.org/)

---
```bash
git clone https://github.com/your-username/aruco-cube-ar.git
cd aruco-cube-ar
```

```bash
pip install -r requirements.txt
```

## Key Concepts Demonstrated

Real-time computer vision processing

Multi-marker AR detection and tracking

6-DOF pose estimation

Camera calibration (intrinsic matrix usage)

3D-to-2D projection transformations

Manual AR rendering without game engines
