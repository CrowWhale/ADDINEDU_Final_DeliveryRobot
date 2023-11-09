import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import String
import cv2

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
        if self.msg_data == "카메라" or self.msg_data == "camera" or self.msg_data == "cam":  # 문자 그대로 하는 1번
        # if self.msg_data.lower() in ["카메라", "camera", "cam"]: # 대소문자 구분없이 하는 2번 # lower은 소문자로 변환하는 문자열 매서드
            capture = cv2.VideoCapture(0)
            capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            while cv2.waitKey(33) < 0:
                ret, frame = capture.read()
                cv2.imshow("VideoFrame", frame)

            capture.release()
            cv2.destroyAllWindows()
        else:
            print("카메라 대기중")

            

def main(args=None):
    rp.init(args=args)
    
    node = Subscriber()
    rp.spin(node)
    
    node.destroy_node() # 노드 종료
    rp.shutdown()


if __name__ == '__main__':
    main()
