import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration,PathJoinSubstitution
from launch_ros.actions import Node



def generate_launch_description():
    package_name='robot_launch' #<--- CHANGE ME
    use_ros2_control = LaunchConfiguration('use_ros2_control')
    
    rsp = IncludeLaunchDescription(
            PathJoinSubstitution([FindPackageShare(package_name),'launch','robot.launch.py']),
            launch_arguments={'use_sim_time': 'true','use_ros2_control': 'true'}.items()
    )

    dcmotor_control = Node(
        package='dcmotor_control',
        executable='run_motor'
    )

    audio_capture = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('audio_capture'),'launch','capture.launch.py']),
        launch_arguments={'sample_rate': 48000,'audio_topic': 'mic_audio'}.items()
    )


    audio_play = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('audio_play'),'launch','play.launch.py']),
        launch_arguments={'sample_rate': 48000,'audio_topic': 'app_audio'}.items()
    )

    camera_ros = Node(
        package='camera_ros',
        executable='camera_node',
        output='screen',
        parameters=[{
            'frame_id': 'camera_link_optical',
            'width': 640,
            'height': 480,                
        }]
    )

    # Launch them all!
    return LaunchDescription([
        DeclareLaunchArgument(
        'use_ros2_control',
        default_value='true',
        description='Use ros2_control if true'),
        rsp,
        dcmotor_control,
        audio_capture,
        audio_play,
        camera_ros,
    ])