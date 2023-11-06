from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import TaskResult
from geometry_msgs.msg import PoseWithCovarianceStamped
import time
from rclpy.node import Node
import threading
from std_msgs.msg import Int32
from std_msgs.msg import String
from rclpy.duration import Duration
from nav2_simple_commander.robot_navigator import TaskResult


class FindLocation(Node):
    def __init__(self):
        super().__init__('navigation')
        
        # topic을 subscribe 하기 위해 subscrption을 생성
        self.subscription = self.create_subscription(
            String, # 수신할 메시지 타입 지정
            'topic', # 구독할 토픽의 이름 지정
            self.Location, # 메시지가 도착했을때 실행할 callback 함수 지정
            10 ) # 메세지를 저장하는 버퍼의 크기 설정
        self.subscription  # prevent unused variable warning
        
        
        self.get_logger().info("Waiting command")
        
        # gazebo 연결 설정
        self.nav = BasicNavigator()
        self.nav.waitUntilNav2Active()
        
        # 좌표 설정
        self.goal_pose = PoseStamped()
        self.goal_pose.header.frame_id = 'map'
        self.goal_pose.header.stamp = self.nav.get_clock().now().to_msg()
        
        # 결과값 설정
        self.result = self.nav.getResult()
        
        
    def Location(self,msg):
        self.get_logger().info("You select %s Location" %(msg.data))
        print("msg.data = ",msg.data)
        
        if msg.data == "fuck":
            # 1st location
            self.goal_pose.pose.position.x = 1.024743676185608
            self.goal_pose.pose.position.y = 0.28036895394325256
            self.goal_pose.pose.position.z = 0.002532958984375
            self.goal_pose.pose.orientation.x = 0.0
            self.goal_pose.pose.orientation.y = 0.0
            self.goal_pose.pose.orientation.z = 0.0
            self.goal_pose.pose.orientation.w = 0.0
            
        elif msg.data == "you":
            self.goal_pose.pose.position.x = 1.5416309833526611
            self.goal_pose.pose.position.y = -0.38075682520866394
            self.goal_pose.pose.position.z = -0.001434326171875
            self.goal_pose.pose.orientation.x = 0.0
            self.goal_pose.pose.orientation.y = 0.0
            self.goal_pose.pose.orientation.z = 0.0
            self.goal_pose.pose.orientation.w = 0.0
            
        elif msg.data == "your":
            self.goal_pose.pose.position.x = 1.2454776763916016
            self.goal_pose.pose.position.y = 1.5881965160369873
            self.goal_pose.pose.position.z = -0.001434326171875
            self.goal_pose.pose.orientation.x = 0.0
            self.goal_pose.pose.orientation.y = 0.0
            self.goal_pose.pose.orientation.z = 0.0
            self.goal_pose.pose.orientation.w = 0.0
            
        elif  msg.data == "asshole":
            self.goal_pose.pose.position.x = 0
            self.goal_pose.pose.position.y = 0
            self.goal_pose.pose.position.z = 0
            self.goal_pose.pose.orientation.x = 0.0
            self.goal_pose.pose.orientation.y = 0.0
            self.goal_pose.pose.orientation.z = 0.0
            self.goal_pose.pose.orientation.w = 0.0

        self.nav.goToPose(self.goal_pose)
        while not self.nav.isTaskComplete():
            pass
        
        if self.nav.isTaskComplete():
            print("minibot is %s location arrived!" %(msg.data))
            time.sleep(3)

def main(args=None):
    # Gazebo Setup!
    rclpy.init(args=args)
    
    find_locate = FindLocation()
    rclpy.spin(find_locate)
    rclpy.shutdown()



if __name__ == '__main__':
    main()
