import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    
    def __init__(self):
        super().__init__('sub')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.callback,
            10)
    
    def callback(self, msg):
        self.msg_data = msg.data  # 메시지 데이터를 변수에 저장
        if(self.msg_data=="써"):
            
            print("맞다") 
        else:
            print("틀리다")

def main(args=None):
    rp.init(args=args)
    
    node = Subscriber()
    rp.spin(node)
    
    node.destroy_node() # 노드 종료
    rp.shutdown()


if __name__ == '__main__':
    main()
