import rclpy
from std_msgs.msg import Bool
from std_msgs.msg import Float32
from rclpy.node import Node
import RPi.GPIO as GPIO
import serial
import subprocess

class cam(Node):
    def __init__(self):
        super().__init__('humi_odour')

        self.publisher = self.create_publisher(Bool, '/para', 10)
        self.subscription1 = self.create_subscription(Bool,'/prediction',self.callback1,10)
        self.subscription2 = self.create_subscription(Float32,'/odour',self.callback2,10)
        self.subscription3 = self.create_subscription(Float32,'/humi',self.callback3,10)
        self.humi = 0.0
        self.odour=0.0
        self.var=Bool()
        self.ser=serial.Serial('/dev/ttyACM0')

    def callback2(self,msg):
        self.humi=msg.data
    
    def callback3(self,msg):
        self.odour=msg.data

    def callback1(self, msg):
        if msg.data:
            if self.var:
                self.ser.write(str(2).encode())
            else:
                subprocess.run(['python', 'feedback.py'])
            print(self.var)
            GPIO.output(6, GPIO.LOW)
            self.publish_msg()


    def publish_msg(self):
        self.publisher.publish(self.var)


    def run(self):
        pass
        
        #self.publish_message()
        # rclpy.spin(self.node)
        # self.node.destroy_node()
        # rclpy.shutdown()
            
def main(args=None):
    rclpy.init(args=args)
    
    com = cam()
    while rclpy.ok():

        # Spin once to process callbacks
        #com.run()
        rclpy.spin_once(com)
    com.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
   main()
