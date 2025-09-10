# ros_venv_demo

Demonstration of running different ROS2 nodes in different Python virtual environments.

```bash
# Create virtual environments
./create_venvs.sh

# Build the package
colcon build

# Source the workspace
source install/setup.bash

# Launch the demo
ros2 launch ros_venv_demo demo.launch.py
```

## Output 

```txt
[INFO] [numpy_echo-1]: process started with pid [21278]
[INFO] [numpy_echo-2]: process started with pid [21279]
[numpy_echo-1] [INFO] [1757499388.720716571] [numpy_echo_venv1]: Numpy version: 2.3.3
[numpy_echo-2] [INFO] [1757499388.722447649] [numpy_echo_venv2]: Numpy version: 1.26.4
[numpy_echo-1] [INFO] [1757499389.704724923] [numpy_echo_venv1]: Numpy version: 2.3.3
[numpy_echo-2] [INFO] [1757499389.707807430] [numpy_echo_venv2]: Numpy version: 1.26.4
[numpy_echo-1] [INFO] [1757499390.704893865] [numpy_echo_venv1]: Numpy version: 2.3.3
[numpy_echo-2] [INFO] [1757499390.707725716] [numpy_echo_venv2]: Numpy version: 1.26.4
```