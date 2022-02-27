#!/usr/bin/env python3


import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import HardwareStatus


class MyNode(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher")
        self.hw_status_pub = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.timer = self.create_timer(1, self.pub_hw_status)
        self.get_logger().info("hw status starting")

    def pub_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 12
        msg.are_motors_ready = True
        msg.debug_message = "ayoi"
        self.hw_status_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
