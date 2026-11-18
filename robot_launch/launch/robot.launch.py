from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, Command
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro
import os
print(os.path.join(os.path.join(get_package_share_directory('robot_launch')),'description','robot.urdf.xacro'))
def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    # Check if we are using ros2_control
    use_ros2_control = LaunchConfiguration('use_ros2_control')

    #Process URDF File
    pkg_path = os.path.join(get_package_share_directory('robot_launch'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    robot_description_config = Command(['xacro ', xacro_file, ' use_ros2_control:=', use_ros2_control, ' sim_mode:=', use_sim_time])


    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config,'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time',default_value='false',description='Use sim time if true'),
        DeclareLaunchArgument('use_ros2_control',default_value='true',description='Use ros2_control if true'),
        node_robot_state_publisher
    ])