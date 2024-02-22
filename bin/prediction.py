import RPi.GPIO as GPIO
import time
import serial
import subprocess

sensor = 6
# buzzer = 18
ser=serial.Serial('/dev/ttyACM0')
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setwarnings(False)
# GPIO.setup(buzzer,GPIO.OUT)

# GPIO.output(buzzer,False)
print ("IR Sensor Ready.....")
print (" ")

try: 
   while True:
      if GPIO.input(sensor):
        #   GPIO.output(buzzer,True)
          print ("Object Detected")
      else:
          print ("Object undetected")


except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()