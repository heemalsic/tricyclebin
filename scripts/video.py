# import cv2
# import subprocess

# video_path = '/home/akash/Desktop/juswork.mp4'
# cap = cv2.VideoCapture(video_path)

# if not cap.isOpened():
#     print("Error: Could not open video file.")
#     exit()

# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))

# cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# should_close = False

# def mouse_callback(event, x, y, flags, param):
#     global should_close
#     if event == cv2.EVENT_LBUTTONDOWN:
#         should_close = True

# cv2.setMouseCallback('Video', mouse_callback)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#         continue

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(30) & 0xFF == 27 or should_close:
#         # Run homescreen.py using subprocess
#         subprocess.run(["python3", "/home/akash/Desktop/homescreen.py"])
#         break

# cap.release()
# cv2.destroyAllWindows()

###############################################################

import cv2
import subprocess

video_path = '/home/akash/Desktop/juswork.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

should_close = False

def mouse_callback(event, x, y, flags, param):
    global should_close
    if event == cv2.EVENT_LBUTTONDOWN:
        should_close = True

cv2.setMouseCallback('Video', mouse_callback)

while True:
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow('Video', frame)

    if cv2.waitKey(30) & 0xFF == 27 or should_close:
        # Run homescreen.py using subprocess
        subprocess.run(["python3", "/home/akash/Desktop/homescreen.py"])
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import subprocess
import time

video_path = '/home/akash/Desktop/juswork.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

should_close = False
last_activity_time = time.time()

def mouse_callback(event, x, y, flags, param):
    global should_close
    global last_activity_time
    if event == cv2.EVENT_LBUTTONDOWN:
        should_close = True
        last_activity_time = time.time()

cv2.setMouseCallback('Video', mouse_callback)

while True:
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow('Video', frame)

    # Check if the window is closed or minimized
    window_property = cv2.getWindowProperty('Video', cv2.WND_PROP_AUTOSIZE)
    if window_property < 0:
        should_close = True

    # Check if more than 30 seconds have passed since the last activity
    if time.time() - last_activity_time > 30:
        subprocess.run(["python3", "/home/akash/Desktop/homescreen.py"])
        break

    if cv2.waitKey(30) & 0xFF == 27 or should_close:
        subprocess.run(["python3", "/home/akash/Desktop/homescreen.py"])
        break
        
cap.release()
cv2.destroyAllWindows()
########################################################################








