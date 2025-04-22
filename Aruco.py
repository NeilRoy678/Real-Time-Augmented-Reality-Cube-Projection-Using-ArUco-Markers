import cv2
import numpy as np

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()
camera_matrix = np.array([[1000, 0, 640], [0, 1000, 360], [0, 0, 1]]) 
dist_coeffs = np.zeros((4, 1)) 

cube_points = np.array([
    [0, 0, 0], [0.05, 0, 0], [0.05, 0.05, 0], [0, 0.05, 0],
    [0, 0, -0.05], [0.05, 0, -0.05], [0.05, 0.05, -0.05], [0, 0.05, -0.05] 
], dtype=np.float32)

edges = [(0, 1), (1, 2), (2, 3), (3, 0),  
         (4, 5), (5, 6), (6, 7), (7, 4), 
         (0, 4), (1, 5), (2, 6), (3, 7)]  

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    corners, ids, _ = detector.detectMarkers(gray)

    if ids is not None:
        print("True")
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, camera_matrix, dist_coeffs)

        for i in range(len(ids)):
            rvec, tvec = rvecs[i], tvecs[i]
            img_pts, _ = cv2.projectPoints(cube_points, rvec, tvec, camera_matrix, dist_coeffs)
            img_pts = img_pts.reshape(-1, 2).astype(int)
            for edge in edges:
                cv2.line(frame, tuple(img_pts[edge[0]]), tuple(img_pts[edge[1]]), (0, 255, 0), 2)

    cv2.imshow("Real-Time AR Cube", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()