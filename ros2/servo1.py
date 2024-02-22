import rclpy
from std_msgs.msg import Bool
import RPi.GPIO as GPIO
import time

class ServoControlNode:
    def __init__(self):
        # Initialize ROS 2 node
        rclpy.init()
        self.node = rclpy.create_node('servo_control_node')

        # Set the GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)

        # Set the GPIO pin for the servo
        self.servo_pin = 17  # Replace with the actual GPIO pin you are using

        # Set the PWM parameters
        self.frequency = 50  # Hz
        self.duty_cycle_min = 2.5  # Duty cycle for 0 degrees
        self.duty_cycle_max = 12.5  # Duty cycle for 180 degrees

        # Configure the GPIO pin for PWM
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(self.servo_pin, self.frequency)
        self.servo_pwm.start(0)

        # Create a subscriber for the boolean topic
        self.subscription = self.node.create_subscription(
            Bool,
            'servo_control_topic',  # Replace with your desired topic name
            self.callback,
            10  # QoS profile, adjust as needed
        )

    def callback(self, msg):
        # Callback function to handle received boolean messages
        if True:#msg.data:  # If the received value is True (1), rotate to 50 degrees
            self.set_servo_position(50)
        else:  # If the received value is False (0), rotate to 0 degrees
            self.set_servo_position(0)

    def set_servo_position(self, angle):
        # Convert angle to duty cycle
        duty_cycle = self.duty_cycle_min + (self.duty_cycle_max - self.duty_cycle_min) * angle / 180.0
        self.servo_pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(1)  # Adjust this delay as needed

    def spin(self):
        # Spin the node to handle callbacks
        rclpy.spin(self.node)

    def destroy_node(self):
        # Clean up GPIO on exit
        self.servo_pwm.stop()
        GPIO.cleanup()
        self.node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    servo_node = ServoControlNode()
    servo_node.spin()
    servo_node.destroy_node()
