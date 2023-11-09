import pyrealsense2 as rs
import cv2
import numpy as np

# RealSense 카메라를 초기화합니다.
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# 카메라 시작
pipeline.start(config)

try:
    while True:
        # 프레임을 얻어옵니다.
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        x = 320  # 원하는 x 좌표
        y = 220  # 원하는 y 좌표

        # (x, y) 위치에서의 깊이 값을 얻습니다.
        depth_value = depth_frame.get_distance(x, y)

        # 깊이 프로필을 가져옵니다.
        depth_profile = depth_frame.get_profile()
        color_profile = color_frame.get_profile()

        # (x, y) 좌표를 실세계 좌표로 변환합니다.
        depth_intrinsics = depth_profile.as_video_stream_profile().get_intrinsics()
        depth_to_color_extrinsics = depth_profile.get_extrinsics_to(color_profile)
        depth_point = rs.rs2_deproject_pixel_to_point(depth_intrinsics, [x, y], depth_value)
        depth_point_in_color = rs.rs2_transform_point_to_point(depth_to_color_extrinsics, depth_point)

        # 깊이 값을 절반으로 나눕니다
        halved_depth_value = depth_value / 2

        # 픽셀 좌표 (x, y)를 절반으로 줄인 깊이 값으로 변환합니다
        depth_point_halved = rs.rs2_deproject_pixel_to_point(depth_intrinsics, [x, y], halved_depth_value)
        depth_point_in_color_halved = rs.rs2_transform_point_to_point(depth_to_color_extrinsics, depth_point_halved)

        # 비디오 스트림을 얻어옵니다.
        color_data = np.asanyarray(color_frame.get_data())

        # 비디오 스트림을 화면에 표시합니다.
        cv2.imshow('RealSense Color Stream', color_data)

        # 3D 좌표를 출력합니다
        print(f"({x}, {y}) 위치의 실측값: ({depth_point_in_color[0]}, {depth_point_in_color[1]}, {depth_point_in_color[2]})")
        # print(f"({x}, {y}) 위치의 실측값 (절반 깊이): ({depth_point_in_color_halved[0]}, {depth_point_in_color_halved[1]}, {depth_point_in_color_halved[2]}")

        # "q" 키를 누르면 종료합니다.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()