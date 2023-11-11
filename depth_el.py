import cv2
import pyrealsense2 as rs
import numpy as np


class Depth_Camera():

    def __init__(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.align = rs.align(rs.stream.color)
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 6)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 6)
        self.toggle = 0  # 초기값을 0으로 설정

    def execute(self):
        try:
            self.pipeline.start(self.config)
        except:
            print("카메라 연결 안됨")
            return

        try:
            while True:
                frames = self.pipeline.wait_for_frames()
                aligned_frames = self.align.process(frames)
                depth_frame = aligned_frames.get_depth_frame()

                x, y = 320, 240
                depth_el = round(depth_frame.get_distance(x, y), 2)
                print("엘리베이터와의 거리: ", depth_el, "m")

                if depth_el >= 0.3 :
                    print("엘리베이터 열림")
                    self.toggle = 1  # 거리가 30 이상이면 toggle에 1 저장
                else:
                    # print("엘리베이터 닫힘")
                    self.toggle = 0  # 거리가 30 미만이면 toggle에 0 저장

                color_image = np.asanyarray(aligned_frames.get_color_frame().get_data())
                cv2.imshow('RealSense', cv2.circle(color_image, (x, y), 2, (0, 0, 255), -1))

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            self.pipeline.stop()

if __name__ == "__main__":
    depth_camera = Depth_Camera()
    depth_camera.execute()
