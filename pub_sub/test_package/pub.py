import rclpy
from rclpy.node import Node



from std_msgs.msg import String


class Publisher(Node):
    def __init__(self):
        super().__init__('pub')  # ROS 2 노드를 초기화하고 이름을 'pub'으로 설정
        self.publisher_ = self.create_publisher(String, 'topic', 10)  
# 'topic' 토픽에 String 메시지를 발행하는 게시자 생성
        timer_period = 0.5  # 메시지 발행 주기를 0.5초로 설정
        self.timer = self.create_timer(timer_period, self.callback)  # 주기적으로 callback 메서드를 호출하는 타이머 생성

    def callback(self):
        msg = String()  # String 메시지 생성
        msg.data = "써"  # 메시지 데이터를 "fuck"로 설정
        self.publisher_.publish(msg)  # 메시지를 게시
        print(msg)  # 메시지를 콘솔에 출력

def main(args=None):
    rclpy.init(args=args)  # ROS 2 노드 시스템 초기화

    node = Publisher()  # Publisher 클래스의 객체를 생성하여 ROS 2 노드를 생성

    rclpy.spin(node)  # 노드를 실행하고 메시지 발행을 계속 수행

    node.destroy_node()  # 노드 정리
    rclpy.shutdown()  # ROS 2 종료

if __name__ == '__main__':
    main()  # 스크립트가 직접 실행될 때 main 함수를 호출하여 노드를 실행