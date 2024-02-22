import RPi.GPIO as GPIO
import time
import rclpy
from std_msgs.msg import Bool

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the IR sensor
ir_sensor_pin = 6

# Set up the GPIO pin as input
GPIO.setup(ir_sensor_pin, GPIO.IN)

def ir_sensor_publisher():
    rclpy.init()
    node = rclpy.create_node('ir_sensor_publisher')

    # Create a publisher for the Bool topic
    publisher = node.create_publisher(Bool, 'ir_sensor_topic', 10)

    msg = Bool()

    try:
        while rclpy.ok():
            # Read the state of the IR sensor
            ir_state = GPIO.input(ir_sensor_pin)


            # Update the Bool message
            msg.data = bool(ir_state)

            # Publish the message
            publisher.publish(msg)

            # Print the state (optional)
            if ir_state:
                print("Obstacle detected!")
            else:
                print("No obstacle.")

            # Wait for a short duration before publishing again
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

    finally:
        # Clean up GPIO on exit
        GPIO.cleanup()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    ir_sensor_publisher()
