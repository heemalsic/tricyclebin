import firebase_admin
from firebase_admin import credentials, firestore
# import RPi.GPIO as GPIO
import time
import rclpy
from std_msgs.msg import Float32

# Set the GPIO mode to BCM
# GPIO.setmode(GPIO.BCM)

# # Define GPIO pins for the ultrasonic sensors
# trig_pin1, echo_pin1 = 23, 24  # Sensor 1
# trig_pin2, echo_pin2 = 17, 27  # Sensor 2
# trig_pin3, echo_pin3 = 5, 6    # Sensor 3

# # Set up the GPIO pins for each sensor
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
    return 62

def print_firebase_data():
    db = firestore.client()
    
    # Retrieve data from Firebase for each sensor
    doc_ref1 = db.collection('distance_data').document('sensor_data_1')
    data1 = doc_ref1.get().to_dict()
    distance1 = data1.get('distance', 0)

    doc_ref2 = db.collection('distance_data').document('sensor_data_2')
    data2 = doc_ref2.get().to_dict()
    distance2 = data2.get('distance', 0)

    doc_ref3 = db.collection('distance_data').document('sensor_data_3')
    data3 = doc_ref3.get().to_dict()
    distance3 = data3.get('distance', 0)

    # Print the distances retrieved from Firebase
    print(f"Distance Sensor 1 (from Firebase): {distance1:.2f} cm")
    print(f"Distance Sensor 2 (from Firebase): {distance2:.2f} cm")
    print(f"Distance Sensor 3 (from Firebase): {distance3:.2f} cm")

def main():
    rclpy.init()
    node = rclpy.create_node('distance_publisher')

    # Create a publisher for the Float32 topic
    publisher = node.create_publisher(Float32, 'ultrasonic_distance', 10)

    msg = Float32()

    try:
        while rclpy.ok():
            # # Measure distance for each sensor
            # dist1 = measure_distance(0,0)
            # dist2 = measure_distance(0,0)
            # dist3 = measure_distance(1,2)

            # Update the Float32 messages
            # msg1 = Float32()
            # msg1.data = float(dist1)

            # msg2 = Float32()
            # msg2.data = float(dist2)

            # msg3 = Float32()
            # msg3.data = float(dist3)

            # Print the distances (optional)
            # print(f"Distance Sensor 1: {dist1:.2f} cm")
            # print(f"Distance Sensor 2: {dist2:.2f} cm")
            # print(f"Distance Sensor 3: {dist3:.2f} cm")

            # Send the distance data to Firebase for each sensor
            # db = firestore.client()
            # doc_ref1 = db.collection('distance_data').document('sensor_data_1')
            # doc_ref1.set({'distance': dist1})

            # doc_ref2 = db.collection('distance_data').document('sensor_data_2')
            # doc_ref2.set({'distance': dist2})

            # doc_ref3 = db.collection('distance_data').document('sensor_data_3')
            # doc_ref3.set({'distance': dist3})

            print_firebase_data()

            # Wait for a short duration before publishing again
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        # Clean up GPIO on exit
        # GPIO.cleanup()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
