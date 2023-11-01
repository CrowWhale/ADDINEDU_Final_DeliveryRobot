import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Publisher(Node):

    def __init__(self):
        super().__init__('pub')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.callback)
        

    def callback(self):
        msg = String()  # String 메시지 생성
        msg.data = "fuck"  # 메시지 데이터 설정
        self.publisher_.publish(msg)  # 메시지 게시
        print(msg)
        
        
def main(args=None):
    rclpy.init(args=args)

    node = Publisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()