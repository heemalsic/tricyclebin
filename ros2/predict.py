import rclpy
from std_msgs.msg import Bool
from ultralytics import YOLO
from picamera2 import Picamera2
picam2=Picamera2()
def ir_sensor_callback(msg):
    #picam2 = Picamera2()
    print(msg.data)
    if msg.data:
        print("Obstacle detected!")
        img = "/home/akash/SIH/picam_temp/test.jpg"

        
        picam2.start_and_capture_file(img)
        picam2.stop()

        model_path = "/home/akash/SIH/weights/train512.pt"

        model = YOLO(model_path)
        names = model.names

        results = model(img, save = True)

        
        for r in results:
	        for c in r.boxes.cls:
		        print(names[int(c)])
    else:
        print("No obstacle.")

def ir_sensor_subscriber():
    rclpy.init()
    node = rclpy.create_node('ir_sensor_subscriber')

    # Create a subscriber for the Bool topic
    subscriber = node.create_subscription(
        Bool,
        'ir_sensor_topic',  # Replace with your desired topic name
        ir_sensor_callback,
        10  # QoS profile, adjust as needed
    )

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    ir_sensor_subscriber()
