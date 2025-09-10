import rclpy
from rclpy.node import Node
import numpy as np

class NumpyEchoNode(Node):
    def __init__(self):
        super().__init__('numpy_echo_node')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f'Numpy version: {np.__version__}')

def main():
    rclpy.init()
    node = NumpyEchoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
