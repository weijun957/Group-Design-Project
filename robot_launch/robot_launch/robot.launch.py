from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    colors = {
        'background_r': '200'
    }

    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('audio_capture'),
                'launch',
                'capture.launch.py'
            ]),
            launch_arguments={
                'device': 'hw:1,0',
                'sample_rate': '48000',
            }.items()
        )
    ])