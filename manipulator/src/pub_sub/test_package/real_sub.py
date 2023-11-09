from math import exp
import os
import rclpy
import select
import sys
import threading
import time

from open_manipulator_msgs.msg import KinematicsPose, OpenManipulatorState
from open_manipulator_msgs.srv import SetJointPosition, SetKinematicsPose
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from std_msgs.msg import Float32

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

present_kinematics_pose = [0.0, 0.0, 0.0]   # 현재 위치
goal_kinematics_pose = [0.0, 0.0, 0.0]   # 목적지 위치
timer = 0
toggle = 0
state = 0

some_distance = 0.01  # meter
task_position_x = 0.01  # meter
task_position_y = 0.01  # meter
task_position_z = 0.01  # meter
path_time = 2.0  # second

up_location = [0.0, 0.0, 0.0]  # 버튼중심점의 x, y, z가 저장됨(가정)(data1)
client_address = [0, 0]  # 목적지의 층수, 1호/2호가 저장됨(가정)(data1)
down_location = [0.0, 0.0, 0.0]  # 버튼중심점의 x, y, z가 저장됨(가정)(data)
button_1 = [0.0, 0.0, 0.0]  # 층수버튼 중심점의 x, y, z 저장됨(가정)(data)
button_2 = [0.0, 0.0, 0.0]  # 층수버튼 중심점의 x, y, z 저장됨(가정)(data)
button_3 = [0.0, 0.0, 0.0]  # 층수버튼 중심점의 x, y, z 저장됨(가정)(data)
button_4 = [0.0, 0.0, 0.0]  # 층수버튼 중심점의 x, y, z 저장됨(가정)(data)
led_number = [0, 0, 0, 0]  # 엘리베이터가 몇층에 있는지 확인 (ex. 2층 -> [0, 1, 0, 0])
robot_reached = 0  # 지도의 절대좌표로 도착했을 시 1로 바뀜   ## 혹은 현재 로봇의 위치랑 도착해야하는 절대위치 가져와서 같을경우 비교&toggle switch 만들거나
prev_goal_kinematics_pose = [0.0, 0.0, 0.0]

class TeleopSubscriber(Node):

    qos = QoSProfile(depth=10)
    settings = None
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    def __init__(self):

        super().__init__('teleop_sub')
        self.node = self
        self.subscription = self.create_subscription(String,'topic',self.real_callback,10)

        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.fake_callback)

        # Create kinematics_pose subscriber
        self.kinematics_pose_subscription = self.create_subscription(
            KinematicsPose,
            'kinematics_pose',
            self.kinematics_pose_callback,
            self.qos)
        self.kinematics_pose_subscription

        # Create manipulator state subscriber
        self.open_manipulator_state_subscription = self.create_subscription(
            OpenManipulatorState,
            'states',
            self.open_manipulator_state_callback,
            self.qos)
        self.open_manipulator_state_subscription

        # Create Service Clients
        self.goal_task_space = self.create_client(SetKinematicsPose, 'goal_task_space_path')
        self.tool_control = self.create_client(SetJointPosition, 'goal_tool_control')
        self.goal_task_space_req = SetKinematicsPose.Request()
        self.tool_control_req = SetJointPosition.Request()
        
    def send_goal_task_space(self, path_time):
        self.goal_task_space_req.end_effector_name = 'gripper'
        self.goal_task_space_req.kinematics_pose.pose.position.x = goal_kinematics_pose[0]
        self.goal_task_space_req.kinematics_pose.pose.position.y = goal_kinematics_pose[1]
        self.goal_task_space_req.kinematics_pose.pose.position.z = goal_kinematics_pose[2]
        self.goal_task_space_req.path_time = path_time

        try:
            self.goal_task_space.call_async(self.goal_task_space_req)
        except Exception as e:
            self.get_logger().info('Sending Goal Kinematic Pose failed %r' % (e,))

    def fake_callback(self):
        with open('/home/boma/state.txt', 'r') as f:
            state = f.read()
            state = int(state)
            if state == 1:
                msg = String()
                self.msg_data = msg.data
                msg.data = "bye"  # 메시지 데이터 설정
                self.publisher_.publish(msg)  # 메시지 게시
                print(msg)
                with open('/home/boma/state.txt', 'w') as f:
                    f.write('2')


    def real_callback(self, msg):
        global some_distance
        global up_location
        global path_time
        global button_1
        global button_2
        global button_3
        global button_4
        global led_number
        global robot_reached
        global toggle
        global state
        global timer

        print(goal_kinematics_pose[0],goal_kinematics_pose[1],goal_kinematics_pose[2])
        print(present_kinematics_pose[0],present_kinematics_pose[1],present_kinematics_pose[2])
        print(up_location[0],up_location[1],up_location[2])

        self.msg_data = msg.data

        up_location = msg
        
        up_location = str(up_location)
        up_location = up_location.split(" ")
        up_location = up_location[1]
        up_location = up_location.split("'")
        up_location = up_location[0]
        up_location = up_location.split(",")
        # up_location = up_location.split(",")
        up_location[0] = float(up_location[0])
        up_location[1] = float(up_location[1])
        up_location[2] = float(up_location[2]) 
        
        # if up_location != 0:
        #     if timer == 0:
        #         timer = 100
        #     elif timer != 0:
        #         timer -= 1
        #     elif timer < 70:
        goal_kinematics_pose[0] = present_kinematics_pose[0] + up_location[2]
        goal_kinematics_pose[1] = present_kinematics_pose[1] + up_location[1]
        goal_kinematics_pose[2] = present_kinematics_pose[2] + up_location[0]
        self.node.send_goal_task_space(path_time)
        print(goal_kinematics_pose[0],goal_kinematics_pose[1],goal_kinematics_pose[2])
        print(present_kinematics_pose[0],present_kinematics_pose[1],present_kinematics_pose[2])
        print(up_location[0],up_location[1],up_location[2])

            







        # # print('일 함')
        #   # 메시지 데이터를 변수에 저장
        # with open('/home/boma/state.txt', 'r') as f:
        #     state = f.read()
        #     state = int(state)
        #     if state == 5:
        #     # if (self.msg_data == "pixel_data setting done"):
        #         with open('/home/boma/pixel_data.txt', 'r') as f:
        #             up_location = f.read()
        #             up_location = up_location.replace("\n", "")
        #             up_location = up_location.split(', ')
        #             up_location[0] = float(up_location[0]) 
        #             up_location[1] = float(up_location[1]) 
        #             up_location[2] = float(up_location[2]) 
        #             if up_location != 0:
        #                 if timer == 0:
        #                     timer = 100
        #                     timer -= 1
        #                 elif timer < 70:
        #                     goal_kinematics_pose[0] = present_kinematics_pose[0] + up_location[0]
        #                     goal_kinematics_pose[1] = present_kinematics_pose[1] + up_location[1]
        #                     goal_kinematics_pose[2] = present_kinematics_pose[2] + up_location[2]
        #                     self.node.send_goal_task_space(path_time)
        #                     with open('/home/boma/pixel_data.txt', 'w') as f:
        #                         f.write('0')
                            




        # with open('/home/boma/state.txt', 'r') as f:
        #         state = f.read()
        #         state = int(state)
        #         if state == 0:
        #             if (self.msg_data == "hi"):
        #                 print('hi')
        #                 with open('/home/boma/state.txt', 'w') as f:
        #                     f.write('1')
        #         elif state == 1:





        # if toggle == 0:
        #     if (self.msg_data == "home"):
        #         goal_kinematics_pose[0] = 0.126
        #         goal_kinematics_pose[1] = -0.076
        #         goal_kinematics_pose[2] = 0.116
        #         self.node.send_goal_task_space(path_time)
        #         print('기본자세로 옴')

        #         msg.data = "back"  # 메시지 데이터 설정
        #         self.publisher_.publish(msg)  # 메시지 게시
        #         print(msg)
        # #         toggle = 1

        # if toggle == 1:
        #     msg = String()  # String 메시지 생성
        #     msg.data = "come"  # 메시지 데이터 설정
        #     self.publisher_.publish(msg)  # 메시지 게시
        #     print(msg)
        #     toggle = 2


        # elif (self.msg_data == "catch"):
        #     with open('/home/boma/pixel_data.txt', 'r') as f:
        #         up_location = f.read()
        #         up_location = up_location.replace("\n", "")
        #         up_location = up_location.split(', ')
        #         up_location[0] = float(up_location[0]) 
        #         up_location[1] = float(up_location[1]) 
        #         up_location[2] = float(up_location[2]) 
        #         if up_location != 0:
        #             if timer == 0:
        #                 timer = 100
        #                 timer -= 1
        #             elif timer > 80:
        #                 goal_kinematics_pose[0] = present_kinematics_pose[0] + up_location[0]
        #                 goal_kinematics_pose[1] = present_kinematics_pose[1] + up_location[1]
        #                 goal_kinematics_pose[2] = present_kinematics_pose[2] + up_location[2]

        #             goal_kinematics_pose[0] = present_kinematics_pose[0] + up_location[0]
        #             goal_kinematics_pose[1] = present_kinematics_pose[1] + up_location[1]
        #             goal_kinematics_pose[2] = present_kinematics_pose[2] + up_location[2]
        #             self.node.send_goal_task_space(path_time)
        #             with open('/home/boma/state.txt', 'w') as f:
        #                 f.write('0')

        # elif (self.msg_data == "stay1"):

        #     print('일 다 함')
        #     with open('/home/boma/state.txt', 'w') as f:
        #         f.write('0')

        # elif (self.msg_data == "push"):
            
        #     print('일 다 함')
        #     with open('/home/boma/state.txt', 'w') as f:
        #         f.write('0')

        # elif (self.msg_data == "stay2"):
            
        #     print('일 다 함')
        #     with open('/home/boma/state.txt', 'w') as f:
        #         f.write('0')

        # elif (self.msg_data == "stay3"):
            
        #     print('일 다 함')
        #     with open('/home/boma/state.txt', 'w') as f:
        #         f.write('0')

        # elif (self.msg_data == "turn"):
            
        #     print('일 다 함')
        #     with open('/home/boma/state.txt', 'w') as f:
        #         f.write('0')

        # elif (self.msg_data == "grap"):
            
        #     print('일 다 함')
        #     with open('/home/boma/state.txt', 'w') as f:
        #         f.write('0')



    # 목적지 넣습니다.
    def kinematics_pose_callback(self, msg):
        present_kinematics_pose[0] = msg.pose.position.x
        present_kinematics_pose[1] = msg.pose.position.y
        present_kinematics_pose[2] = msg.pose.position.z

    # 멈춰있을때, 현재 위치를 담습니다.
    def open_manipulator_state_callback(self, msg):
        if msg.open_manipulator_moving_state == 'STOPPED':
            for index in range(0, 3):
                goal_kinematics_pose[index] = present_kinematics_pose[index]


def main(args=None):
    settings = None

    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    try:
        rclpy.init(args=args)
    except Exception as e:
        print(e)
        return

    try:
        node = TeleopSubscriber()
        rclpy.spin(node)  # Spin the node
    except Exception as e:
        print(e)

    finally:
        if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()










        # elif (self.msg_data == "catch"):
        #     with open('/home/boma/pixel_data.txt', 'r') as f:
        #         up_location = f.read()
        #         up_location = up_location.replace("\n", "")
        #         up_location = up_location.split(', ')
        #         print('in the third', up_location[0])
        #         up_location[0] = float(up_location[0]) 
        #         up_location[1] = float(up_location[1]) 
        #         up_location[2] = float(up_location[2]) 
        #         # print(up_location)
        #         print(type(up_location))
        #         if up_location != 0:
        #             goal_kinematics_pose[0] = present_kinematics_pose[0] + up_location[0]
        #             goal_kinematics_pose[1] = present_kinematics_pose[1] + up_location[1]
        #             goal_kinematics_pose[2] = present_kinematics_pose[2] + up_location[2]
        #             self.node.send_goal_task_space(path_time)
        #             with open('/home/boma/state.txt', 'w') as f:
        #                 f.write('0')


                #     with open('/home/boma/state.txt', 'r') as f:
                # state = f.read()
                # state = float(state)
                # if state != 0:
                #     goal_kinematics_pose[0] = 0.044
                #     goal_kinematics_pose[1] = 0.044
                #     goal_kinematics_pose[2] = 0.044
                #     self.node.send_goal_task_space(path_time)
                #     print('기본자세로 옴')
                #     with open('/home/boma/state.txt', 'w') as f:
                #         f.write('0')