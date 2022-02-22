#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStationNode : public rclcpp::Node
{

public:
    RobotNewsStationNode() : Node("robot_news_station")
    {
        publisher=this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
        timer = this->create_wall_timer(std::chrono::seconds(1), std::bind(&RobotNewsStationNode::publish_news, this));
        RCLCPP_INFO(this->get_logger(), "heyo rbot news node");
    }

private:
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher;

    void publish_news()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = "herro";
        publisher -> publish(msg);
    }
    rclcpp::TimerBase::SharedPtr timer;
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}