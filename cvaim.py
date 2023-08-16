import cv2
import numpy as np
import win32api
import win32con

# lowerbound = np.array([0, 100, 100]) for red
# upperbound = np.array([10, 255, 255])
lowerbound = np.array([35, 100, 100]) #for green
upperbound = np.array([85, 255, 255])
cap = cv2.VideoCapture(0)
while True:
  
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerbound, upperbound)
    contours, _ = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE, cx * 65535 // frame.shape[1], cy * 65535 // frame.shape[0], 0, 0)
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()