import rclpy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO
import time

class ROS2Subscriber:
    def __init__(self, node_name, topic_name):
        self.node = rclpy.create_node(node_name)
        self.subscription = self.node.create_subscription(
            Int32,
            topic_name,
            self.callback,
            10  # QoS profile depth
        )
        print(f"Subscribing to topic '{topic_name}'...")
        self.in1 = 17
        self.in2 = 18
        self.in3 = 27
        self.in4 = 22
        self.step_sleep = 0.002

        self.step_count = 0 # 5.625*(1/64) per step, 4096 steps is 360°
        self.angle = abs(4096/360)
        self.direction = False # True for clockwise, False for counter-clockwise

        # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
        self.step_sequence = [[1,0,0,1],
                         [1,0,0,0],
                         [1,1,0,0],
                         [0,1,0,0],
                         [0,1,1,0],
                         [0,0,1,0],
                         [0,0,1,1],
                         [0,0,0,1]]
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( self.in1, GPIO.OUT )
        GPIO.setup( self.in2, GPIO.OUT )
        GPIO.setup( self.in3, GPIO.OUT )
        GPIO.setup( self.in4, GPIO.OUT )

        # initializing
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        self.motor_pins = [self.in1,self.in2,self.in3,self.in4]
        self.motor_step_counter = 0
    def cleanup(self):
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        GPIO.cleanup()

    def callback(self, msg):
        print("Received: {}".format(msg.data))
        if msg.data:
            self.step_count=self.angle*120
        elif msg.data==2:
            self.step_count=self.sngle*120
        else:
            self.step_count=0
    

    def servo(self):
        try:
            rclpy.spin(self.node)
        except KeyboardInterrupt:
            print("KeyboardInterrupt, shutting down...")
        finally:
            self.node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    rclpy.init()

    # Create an instance of the ROS2Subscriber class
    ros2_subscriber = ROS2Subscriber(node_name='my_ros2_node', topic_name='my_topic')

    # Run the ROS 2 node
    ros2_subscriber.servo()
