from launch import LaunchDescription
from launch_ros.actions import Node
from os import pathsep
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    
    lgbot_description = get_package_share_directory("lg-robot")
    lgbot_description_prefix = get_package_prefix("lg-robot")

    model_path = os.path.join(lgbot_description, "models")
    model_path += pathsep + os.path.join(lgbot_description_prefix, "share")

    env_variable = SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path)

    # controller=os.path.join(get_package_share_directory("lg-robot"),'config','lg_robot_controllers.yaml')

    model_args = DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(get_package_share_directory("lg-robot"), "urdf", "lgrobot.urdf.xacro"),
        description="Absolute path to the robot URDF file"
    )

    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model")]), value_type=str)
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}]
    )

    start_gazebo_server = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(
        get_package_share_directory("gazebo_ros"), "launch", "gzserver.launch.py"
    )))
    start_gazebo_client = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(
        get_package_share_directory("gazebo_ros"), "launch", "gzclient.launch.py"
    )))

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "lgrobot", "-topic", "robot_description"],
        output="screen"
    )
    controller_broadCaster= Node(
          package='controller_manager',
            executable='spawner',
            arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
            output='screen'
    )
    controller_Trajectory_Controller=Node(
            package='controller_manager',
            executable='spawner',
            arguments=['joint_trajectory_controller', '--controller-manager', '/controller_manager'],
            output='screen'
        )
    # controlling_Unit = Node(
    #         package='controller_manager',
    #         executable='ros2_control_node',
    #         parameters=[controller, {'robot_description': robot_description}],
    #         output='screen'
    #     )

    return LaunchDescription([
    env_variable,
    model_args,
    robot_state_publisher,
    start_gazebo_server,
    start_gazebo_client,
    spawn_robot,
    # controlling_Unit, 
    controller_broadCaster,
    controller_Trajectory_Controller
])

