import rclpy
from rclpy.node import Node
from gpiozero import Motor
import time
from std_msgs.msg import String
class MotorControl(Node):
    def __init__(self):
        super().__init__('motor_control')
        self.rwheel=Motor(17,27)
        self.lwheel=Motor(22,23)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Forward')
        self.rwheel.forward(1)
        self.lwheel.forward(1)
        time.sleep(10)
        self.get_logger().info('Backward')
        self.rwheel.backward(1)
        self.lwheel.backward(1)
        time.sleep(5) 
        self.get_logger().info('Left')
        self.rwheel.forward(1)
        self.lwheel.backward(1)
        time.sleep(10)
        self.get_logger().info('Right')
        self.rwheel.backward(1)
        self.lwheel.forward(1)
        time.sleep(5)
        self.get_logger().info('Stop')
        self.rwheel.stop()
        self.lwheel.stop()
        time.sleep(5)  

def main(args=None):
    rclpy.init(args=args)
    motor_run = MotorControl()
    rclpy.spin(motor_run)

    self.rwheel.close()
    self.lwheel.close()
    motor_run.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
