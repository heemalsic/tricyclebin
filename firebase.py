import firebase_admin
from firebase_admin import credentials, firestore
# import RPi.GPIO as GPIO
import time
import rclpy
from std_msgs.msg import Float32
from  rclpy.node import Node 



# # Set the GPIO mode to BCM
# GPIO.setmode(GPIO.BCM)

# # Define GPIO pins for the ultrasonic sensor
# trig_pin1, echo_pin1 = 23, 24  # Sensor 1
# trig_pin2, echo_pin2 = 17, 27  # Sensor 2
# trig_pin3, echo_pin3 = 5, 6    # Sensor 3

# # Set up the GPIO pins
# GPIO.setup(trig_pin1, GPIO.OUT)
# GPIO.setup(echo_pin1, GPIO.IN)
# GPIO.setup(trig_pin2, GPIO.OUT)
# GPIO.setup(echo_pin2, GPIO.IN)
# GPIO.setup(trig_pin3, GPIO.OUT)
# GPIO.setup(echo_pin3, GPIO.IN)

# Initialize Firebase with your credentials
cred = credentials.Certificate("/home/akash/Desktop/firebase.json")
firebase_admin.initialize_app(cred)

def measure_distance(trig_pin, echo_pin):
    return 55



def main():
    rclpy.init()
    node = rclpy.create_node('distance_subscriber')

    # Create a publisher for the Float32 topic
    
    subscription1 = Node.create_subscription(
        Float32,
        'ult1',
        callback1,
        10)
    subscription2 = Node.create_subscription(
        Float32,
        'ult2',
        callback2,
        10)
    subscription3 = Node.create_subscription(
        Float32,
        'ult3',
        callback3,
        10)


    msg = Float32()

    try:
        while rclpy.ok():
            # Measure distance
            dist = measure_distance(trig_pin1, echo_pin1)
            dist1 = measure_distance(trig_pin2, echo_pin2)
            dist2 = measure_distance(trig_pin3, echo_pin3)

            # Update the Float32 message
            msg1 = Float32()
            msg1.data = float(dist)

            msg2 = Float32()
            msg2.data = float(dist1)

            msg3 = Float32()
            msg3.data = float(dist2)

            # Print the distance (optional)
            print(f"Distance Sensor 1: {dist:.2f} cm")
            print(f"Distance Sensor 2: {dist1:.2f} cm")
            print(f"Distance Sensor 3: {dist2:.2f} cm")

            # Send the distance data to Firebase
            db = firestore.client()
            doc_ref = db.collection('distance_data').document('sensor_data')
            doc_ref.set({'distance': dist})

            db = firestore.client()
            doc_ref = db.collection('distance_data').document('sensor_data1')
            doc_ref.set({'distance': dist1})

            db = firestore.client()
            doc_ref = db.collection('distance_data').document('sensor_data2')
            doc_ref.set({'distance': dist2})

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
    main()
