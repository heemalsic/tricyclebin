import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the servo signal
servo_pin = 17

# Set the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object with a frequency of 50Hz
pwm = GPIO.PWM(servo_pin, 50)

# Start PWM with a duty cycle of 7.5% (neutral position for a continuous servo)
pwm.start(7.5)

try:
    while True:
        # Rotate the servo clockwise
        pwm.ChangeDutyCycle(10)
        time.sleep(2)

        # Rotate the servo counterclockwise
        pwm.ChangeDutyCycle(5)
        time.sleep(2)

except KeyboardInterrupt:
    # If Ctrl+C is pressed, cleanup and exit
    pwm.stop()
    GPIO.cleanup()