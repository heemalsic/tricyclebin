from ultralytics import YOLO
from picamera2 import Picamera2

var=0

img = "/home/akash/SIH/picam_temp/test.jpg"

picam2 = Picamera2()
picam2.start_and_capture_file(img)

model_path = "/home/akash/SIH/weights/train547.pt"

model = YOLO(model_path)
names = model.names

results = model(img, save = True)

list = []
# print(results)
for r in results:
	for c in r.boxes.cls:
		list.append(names[int(c)])

print(len(list))
b=0
n=0

for i in list:
	if i=='paper_cups':
		b=b+1
	else:
		n=n+1
if (len(list)==b) and (len(list)!=0):
	var=0
elif (len(list)==n) and (len(list)!=0):
	var=1
else:
	var=2
print(var)
