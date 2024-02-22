import rclpy
from std_msgs.msg import Bool
from rclpy.node import Node
from ultralytics import YOLO
from picamera2 import Picamera2
import RPi.GPIO as GPIO


class cam(Node):
    def __init__(self):
        super().__init__('cam')

        self.publisher = self.create_publisher(Bool, '/prediction', 10)
        self.subscription = self.create_subscription(
            Bool,
            '/ir_sensor_topic',
            self.callback,
            10)
        self.var=Bool()
        self.ser=serial.Serial('/dev/ttyACM0')



    def callback(self, msg):
        if msg.data:
            GPIO.output(6, GPIO.HIGH)
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
            b=0
            n=0

            for i in list:
                if i=='paper_cups':
                    b=b+1
                else:
                    n=n+1
            if (len(list)==b) and (len(list)!=0):
                self.ser.write(str(0).encode())
            elif (len(list)==n) and (len(list)!=0):
                self.ser.write(str(1).encode())
            else:
                self.var.data=True
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
