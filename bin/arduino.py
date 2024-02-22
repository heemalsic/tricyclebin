import rclpy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from std_msgs.msg import Bool
import serial
import re
from rclpy.node import Node

class arduino(Node):
    def __init__(self):
        super().__init__('hb_controller')
        self.publisher1 = self.create_publisher(Float32, 'ult1', 10)
        self.publisher2 = self.create_publisher(Float32, 'ult2', 10)
        self.publisher3 = self.create_publisher(Float32, 'ult3', 10)
        self.publisher4 = self.create_publisher(Bool, 'food', 10)
        self.publisher5 = self.create_publisher(Float32, 'humi', 10)
        self.publisher6 = self.create_publisher(Float32, 'temp', 10)
        self.subscription = self.create_subscription(
            Int32,
            'comp',
            self.callback,
            10)
        #self.timer = self.node.create_timer(1.0, self.publish_message)
        self.ser=serial.Serial('/dev/ttyACM0', 9600)
        self.ult1=Float32()
        self.ult2=Float32()
        self.ult3=Float32()
        self.food=Bool()
        self.humi=Float32()
        self.temp=Float32()
        self.comp=0
        self.input_string=str()
        self.ult=int()
        self.value=0.0
        timer_period = 1.0  # seconds
        #self.timer = self.create_timer(timer_period, self.run)


    def extract_number_after_ult(self):
        # Use regular expression to find the number after "ult"
        match = re.search(r'ult(\d+)', self.input_string)

        if match:
            # Extract the matched number and convert it to an integer
            self.ult = int(match.group(1))
            print(self.ult)
        #     return ult_number
        # else:
        #     # Return None if no match is found
        #     return None
    
    def extract_last_number(self):
        # Use regular expression to find the last number in the string
        match = re.search(r':\s*([\d.]+)\s*$', self.input_string)

        if match:
            # Extract the matched number and convert it to float
            self.value = float(match.group(1))
            print(self.value)
        #     return last_number
        # else:
        #     # Return None if no match is found
        #     return None


    def callback(self, msg):
        self.node.get_logger().info('Received: %d' % msg.data)
        if msg.data: 
            self.ser.write(str(0).encode())
        elif msg.data==2:
            self.ser.write(str(1).encode())
        elif msg.data==3:
            self.ser.write(str(2).encode())

    def publish_msg1(self):
        self.publisher1.publish(self.ult1)
    
    def publish_msg2(self):
        self.publisher2.publish(self.ult2)

    def publish_msg3(self):
        self.publisher3.publish(self.ult3)
    
    def publish_msg4(self):
        self.publisher4.publish(self.food)
    def publish_msg5(self):
        self.publisher5.publish(self.humi)
    def publish_msg6(self):
        self.publisher5.publish(self.temp)

    def run(self):
        self.input_string = self.ser.readline().decode('utf-8').strip()
        self.extract_last_number()
        self.extract_number_after_ult()
        if self.ult==1:
            self.ult1.data=self.value
            self.publish_msg1()
        elif self.ult==2:
            self.ult2.data=self.value
            self.publish_msg2()
        elif self.ult==3:
            self.ult3.data=self.value
            self.publish_msg3()
        elif self.ult==4:
            if self.value>17:
                self.food.data=True
            else:
                self.food.data=False 
            self.publish_msg4()
        elif self.ult==5:
            self.humi.data=self.value
        elif self.ult==6:
            self.temp.data=self.value
        
        #self.publish_message()
        # rclpy.spin(self.node)
        # self.node.destroy_node()
        # rclpy.shutdown()
            
def main(args=None):
    rclpy.init(args=args)
    
    com = arduino()
    while rclpy.ok():

        # Spin once to process callbacks
        com.run()
        #rclpy.spin(com)
    com.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
   main()