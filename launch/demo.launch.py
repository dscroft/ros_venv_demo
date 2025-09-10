from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import GroupAction, SetEnvironmentVariable
import os
import sys
from ament_index_python.packages import get_package_share_directory

def gen_environment(venv_base):
    # Get the path to your virtual environment
    #venv_base = "/home/david/Documents/ros_venv_demo/venv_a"
    venv_bin = os.path.join(venv_base, "bin")
    venv_lib = os.path.join(venv_base, "lib")
    # Get the Python version used in the venv
    py_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    venv_python_pkgs = os.path.join(venv_lib, f"{py_version}/site-packages")

    # ROS paths
    ros_base = os.environ.get("ROS_DISTRO_PATH", f"/opt/ros/{os.environ.get('ROS_DISTRO', 'jazzy')}")
    ros_lib = os.path.join(ros_base, "lib")
    ros_python_pkgs = os.path.join(ros_lib, f"{py_version}/site-packages")

    # Home directory for ROS logs
    home_dir = os.path.expanduser("~")
    ros_home = os.path.join(home_dir, ".ros")

    # Combine environment variables
    env = {
        'PATH': f"{venv_bin}:{os.environ.get('PATH', '')}",
        'PYTHONPATH': f"{venv_python_pkgs}:{ros_python_pkgs}:{os.environ.get('PYTHONPATH', '')}",
        'LD_LIBRARY_PATH': f"{venv_lib}:{ros_lib}:{os.environ.get('LD_LIBRARY_PATH', '')}",
        'VIRTUAL_ENV': venv_base,
        # ROS-specific environment variables
        'ROS_HOME': ros_home,
        'ROS_LOG_DIR': os.path.join(ros_home, "log"),
        'HOME': home_dir,  # Ensure HOME is properly set
        'USER': os.environ.get('USER', ''),  # Pass through user name
        'ROS_DOMAIN_ID': os.environ.get('ROS_DOMAIN_ID', '0'),
        'RMW_IMPLEMENTATION': os.environ.get('RMW_IMPLEMENTATION', 'rmw_fastrtps_cpp')
    }

    return env

def generate_launch_description():
    # Get the package share directory
    package_share_dir = get_package_share_directory('ros_venv_demo')
    # Assume venv_a and venv_b are in the package share directory
    venv_a_path = os.path.join(package_share_dir, 'venv_a')
    venv_b_path = os.path.join(package_share_dir, 'venv_b')

    return LaunchDescription([
        Node(
            package='ros_venv_demo',
            executable='numpy_echo',
            name='numpy_echo_venv1',
            output='screen',
            env=gen_environment(venv_a_path)
        ),
        Node(
            package='ros_venv_demo',
            executable='numpy_echo',
            name='numpy_echo_venv2',
            output='screen',
            env=gen_environment(venv_b_path)
        )
    ])