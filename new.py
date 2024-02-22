import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

    def __init__(self):
        super().__init__('my_node')

        # Create a publisher
        self.publisher = self.create_publisher(String, 'my_topic', 10)

        # Create a subscriber
        self.subscriber = self.create_subscription(
            String, 'my_topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        print(f'Received message: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()

    # Publish a message
    msg = String()
    msg.data = 'Hello, world!'
    node.publisher.publish(msg)

    # Keep the node running
    rclpy.spin(node)

    # Close the node
    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()