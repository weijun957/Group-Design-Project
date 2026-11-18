import rclpy
from rclpy.node import Node
from gpiozero import Motor
from geometry_msgs.msg import Twist
from time import sleep

class MotorControl(Node):
    def __init__(self):
        super().__init__('motor_control')
        self.subscription = self.create_subscription(Twist,'/cmd_vel',self.listener_callback,10)

    def listener_callback(self, msg: Twist):
        self.rwheel=Motor(17,27)
        self.lwheel=Motor(22,23)
        linear_x = msg.linear.x
        angular_z = msg.angular.z
        self.get_logger().info(f'Received -> Linear X: {linear_x:.2f}, Angular Z: {angular_z:.2f}')
        if(linear_x>0 and angular_z==0):
            self.get_logger().info('Forward')
            self.rwheel.forward(1)
            self.lwheel.forward(1)
            sleep(1)
        elif(linear_x<0 and angular_z==0):
            self.get_logger().info('Backward')
            self.rwheel.backward(1)
            self.lwheel.backward(1)
            sleep(1)
        elif(linear_x==0 and angular_z==0):
            self.get_logger().info('Stop')
            self.rwheel.stop()
            self.lwheel.stop()
            sleep(1)
        elif(linear_x==0 and angular_z>0):
            self.get_logger().info('Left')
            self.rwheel.forward(1)
            self.lwheel.backward(1)
            sleep(1)
        elif(linear_x==0 and angular_z<0):
            self.get_logger().info('Right')
            self.lwheel.forward(1)
            self.rwheel.backward(1)
            sleep(1)
        self.rwheel.close()
        self.lwheel.close()


def main(args=None):
    rclpy.init(args=args)
    motor_run = MotorControl()
    rclpy.spin(motor_run)
    motor_run.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
