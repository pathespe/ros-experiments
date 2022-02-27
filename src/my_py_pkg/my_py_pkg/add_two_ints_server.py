#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MyNode(Node):

    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server = self.create_service(AddTwoInts, "add_two_ints", self.callback)
        self.get_logger().info("add_two_ints_server starting")

    def callback(self, request, response):
        response.sum = request.a +request.b
        self.get_logger().info(f"{request.a + request.b}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()