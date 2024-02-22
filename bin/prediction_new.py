import rclpy
from std_msgs.msg import Bool
from rclpy.node import Node
from ultralytics import YOLO
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import serial
import subprocess

class cam():
    def _init_(self):
        

        

        
        
        self.ser=serial.Serial('/dev/ttyACM0')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.IN)
        

        self.i=0
        self.array=[1,1,0,2,1]



    def callback(self):
        self.msg=GPIO.input(6)
        if self.msg:
            print("detect")
            if(self.array[self.i]):
                proc1 = subprocess.Popen(['python', 'feedback.py'])
                proc1.wait()

            else:    
                self.ser.write(str(self.array[self.i]).encode())
        
            self.i=self.i+1
            if self.i==3:
                self.i=0
            


    def run(self):
        pass
        
        #self.publish_message()
        # rclpy.spin(self.node)
        # self.node.destroy_node()
        # rclpy.shutdown()
            
def main(args=None):
    rclpy.init(args=args)
    
    com = cam()
    while True:

        # Spin once to process callbacks
        com.callback()
        
    GPIO.cleanup()
    com.destroy_node()
    rclpy.shutdown()


if __name__ == '_main_':
   main()