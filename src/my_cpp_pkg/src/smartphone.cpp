#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class SmartPhoneNode : public rclcpp::Node
{

public:
    SmartPhoneNode() : Node("robot_news_station")
    {
        subscriber = this->create_subscription<example_interfaces::msg::String>(
            "robot_news", 10,
            std::bind(&SmartPhoneNode::callback, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "subbed to robot news");
    }

private:
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher;
    void callback(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SmartPhoneNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}