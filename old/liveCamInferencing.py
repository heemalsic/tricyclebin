import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from ultralytics import YOLO

model_path = "/home/akash/SIH/weights/train686.pt"
model = YOLO(model_path)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, img= cap.read()
    results = model(img, stream=True)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()