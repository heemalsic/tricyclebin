from ultralytics import YOLO
from picamera2 import Picamera2

img = "/home/akash/SIH/picam_temp/test.jpg"

picam2 = Picamera2()
picam2.start_and_capture_file(img)

model_path = "/home/akash/SIH/weights/med_waste.pt"

model = YOLO(model_path)
names = model.names

results = model(img, save = True)

classlist = []
# print(results)
for r in results:
	for c in r.boxes.cls:
		classlist.append(names[int(c)])

message = int()
 
if len(classlist)==0:
    message = 0
     
else:
    message = 1