#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_no_oop")
    client = node.create_client(AddTwoInts, "add_two_ints")

    while not client.wait_for_service(1):
        node.get_logger().warn("waiting for server")

    request = AddTwoInts.Request()
    request.a = 234
    request.b = 6783426
    f = client.call_async(request=request)
    rclpy.spin_until_future_complete(node=node, future=f)
    try:
        resp = f.result()
        node.get_logger().info(f"{resp.sum}")
    except Exception as e:
        node.get_logger().error(f"{e}")
    rclpy.shutdown()
