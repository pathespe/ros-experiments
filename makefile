colcon:
	colcon build

run-cpp:
	ros2 run my_cpp_pkg cpp_node

run-py:
	ros2 run my_py_pkg py_node

build-py:
	colcon build --packages-select my_py_pkg --symlink-install