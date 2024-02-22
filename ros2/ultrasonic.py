import RPi.GPIO as GPIO
import time
import rclpy
from std_msgs.msg import Float32

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the ultrasonic sensor
trig_pin = 23  # GPIO pin for the trigger
echo_pin = 24  # GPIO pin for the echo

# Set up the GPIO pins
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def measure_distance():
    # Trigger the ultrasonic sensor
    GPIO.output(trig_pin, GPIO.LOW)
    time.sleep(2)  # Allow the sensor to settle

    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    # Measure the pulse duration on the echo pin
    pulse_start_time = time.time()
    pulse_end_time = time.time()

    while GPIO.input(echo_pin) == GPIO.LOW:
        pulse_start_time = time.time()

    while GPIO.input(echo_pin) == GPIO.HIGH:
        pulse_end_time = time.time()

    # Calculate the pulse duration and distance
    pulse_duration = pulse_end_time - pulse_start_time
    distance = pulse_duration * 34300 / 2  # Speed of sound is approximately 343 meters/second

    return distance

def distance_publisher():
    rclpy.init()
    node = rclpy.create_node('distance_publisher')

    # Create a publisher for the Float32 topic
    publisher = node.create_publisher(Float32, 'ultrasonic_distance', 10)

    msg = Float32()

    try:
        while rclpy.ok():
            # Measure distance
            dist = measure_distance()

            # Update the Float32 message
            msg.data = float(dist)

            # Publish the message
            publisher.publish(msg)

            # Print the distance (optional)
            print(f"Distance: {dist:.2f} cm")

            # Wait for a short duration before publishing again
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        # Clean up GPIO on exit
        GPIO.cleanup()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    distance_publisher()
