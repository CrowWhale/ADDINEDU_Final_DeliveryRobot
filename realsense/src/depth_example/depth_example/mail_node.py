import os
import sys
from rclpy.node import Node
from sensor_msgs.msg import Image
import rclpy
from std_msgs.msg import String

distance = 0

class MAIL(Node):
    def __init__(self):
        super().__init__('mail')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.pub_callback)

        self.subscription = self.create_subscription(String, 'topic', self.sub_callback, 10)
        self.subscription


    def sub_callback(self, msg):
        self.msg_data = msg.data
        if (self.msg_data == "bye"):
            print('byebye')

    def pub_callback(self):
        global distance

        with open('/home/boma/Desktop/test.txt', 'r') as f:
            number = f.read()
            number = int(number)

        if number == 5:
            with open('/home/boma/pixel_data.txt', 'r') as d:
                distance = d.read()
            #     distance = distance.replace("\n", "")
            #     distance = distance.split(" ")
            #     distance = distance[1]
            #     print('yeah~~', distance)
            msg = String()
            self.msg_data = msg.data
            # distance = distance.replace("\n")
            msg.data = distance  # 메시지 데이터 설정
            self.publisher_.publish(msg)  # 메시지 게시
            print(msg)
            with open('/home/boma/Desktop/test.txt', 'w') as f:
                f.write('0')


def main(args=None):
    rclpy.init(args=args)

    node = MAIL()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()