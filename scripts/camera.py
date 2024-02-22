from picamera2 import Picamera2
# from ultralytics import YOLO

pic = Picamera2()
pic.start_and_capture_file("imag34.jpg")