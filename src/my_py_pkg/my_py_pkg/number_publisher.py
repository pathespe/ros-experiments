#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class MyNode(Node):

    def __init__(self):
        super().__init__("number_publisher")
        self.publisher = self.create_publisher(Int64, "number", 10)
        self.timer = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Number publisher TO THE MOON")

    def publish_news(self):
        msg = Int64()
        msg.data = 69420
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()