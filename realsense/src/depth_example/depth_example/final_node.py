import os
import sys
from rclpy.node import Node
from sensor_msgs.msg import Image
import rclpy
from std_msgs.msg import String


yolo = 'python3' + ' /home/boma/Robot-repo-1/yolov7/detect_final.py' + ' --weights' + ' /home/boma/Robot-repo-1/yolov7/final.pt' + ' --conf-thres 0.6'
qr = 'python3' + ' /home/boma/Desktop/qr.py'

number = 0



class REALSENSE(Node):
    def __init__(self):
        super().__init__('realsesne')



def main(args=None):
   
    while True:
        with open('/home/boma/Desktop/test.txt', 'r') as f:
            number = f.read()
            number = int(number)
            if number == 1:
                os.system(yolo)
                with open('/home/boma/Desktop/test.txt', 'w') as f:
                    f.write('0')
            elif number == 2:
                os.system(qr)
                with open('/home/boma/Desktop/test.txt', 'w') as f:
                    f.write('0')


if __name__ == '__main__':
    main()