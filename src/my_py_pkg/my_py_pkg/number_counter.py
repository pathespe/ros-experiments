#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class MyNode(Node):

    def __init__(self):
        super().__init__("number_counter")
        self.count = 0
        self.publisher = self.create_publisher(Int64, "number_count", 10)
        self.subscriber = self.create_subscription(
            Int64, "number", self.callback, 10
        )
        self.server = self.create_service(SetBool, "reset_counter", self.reset_callback)
        self.get_logger().info("number_counter INITIATED")

    def reset_callback(self, request, response):
        if request.data:
            self.count = 0
            response.success = True
            response.message = "sdasd"
            return response

        self.get_logger().info(f"Reset data: {request.data}")
        response.success = False
        response.message = "nah"
        return response

    def callback(self, msg):
        self.count += msg.data
        msg2 = Int64()
        msg2.data = self.count
        self.publisher.publish(msg2)
        self.get_logger().info(f"{self.count}")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()