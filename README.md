Robot_Delivery
=========

<div align="center">
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/c5d1ed7c-905f-48e6-a4e4-0cad3d4f0f35" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/a8c8ff1d-4b09-4ee2-997a-39cebda308e8" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/7ba7d2a7-7181-4a1b-951f-4657235dc992" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/5f791e00-8687-4b88-ae2a-63cf7c4d0fa8" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/31c6515f-a85c-4e3b-bfeb-5d5ee8533792" width="7%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
  <a>
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-docker-small.png" width="7%" /></a>

</div>

Introduction
=========
### 아파트 내 택배를 자동으로 분류 및 보관하는 STATION과 현관까지 배송해주는 DELIVERY_ROBOT 개발
# Demo
<div align="center">
  <img src="demo.gif"/>
</div>

[『YOUTUBE_FULL_DEMO_VIDEO』](https://www.youtube.com/watch?v=yonJqRplI4o)

# SYSTEM_CONFIGURATION
![Screenshot from 2023-11-14 17-40-37](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/c881aef8-e224-4ff2-b445-d4ea391d142d)
1. 자율주행 part
> * 배송로봇 자율주행 구현(ROS, Mapping, Navigation)
2. Manipulator
> * manipulator 구동 알고리즘(ROS)
> * 이송 객체 크기 인식(Deep Learning, Computer Vision)
3. Station part
> * Station 제작 및 구동 알고리즘(3D modeling & printing, IoT)
4. Computer Vision & 영상처리 part
> * 객체 text 데이터 인식(Computer vision, Image processing)

# SEQUENCE
![왕빵스케치시퀀스](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/1c8ca792-1681-4096-b700-53bde99febdb)

# Software
1. Station 보관 및 Robot 호출
![스테이션](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/12d164d9-4c28-4b72-8314-7c2df1d446bc)
2. 아파트 내 엘리베이터 도착 및 탑승
![엘리베이터](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/595b23e2-877f-4102-b54b-fe6e8f4648d6)
3. 현관 배송 후 복귀
![현관](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/71e1c026-94a1-4638-b2f9-c92e83e073fc)
# Ros Package
![ros_package](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/3e7ac35c-5b86-4f85-abc6-e2ebe4641b74)

# Hardware

## 1. Turtlebot3 & YDLidar
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/2989c886-dfb2-4f39-9778-3609b2a39f12" width="50%" /></a> 


* Referance: [Turtlebot3_e-Maniual](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
### Excute Code
* PC
```
ros2 launch turtlebot3_navigation2 navigation2.launch.py
```
```
ros2 run navigation my_nav
```
* Raseberry Pi
```
ros2 launch turtlebot3_bringup robot.launch.py
```

## 2. Manipulator
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/3eee941e-9710-4f08-aad8-51482dca98db" width="50%" /></a> 


* Referance: [OpenMANIPULATOR-X_e-Maniual](https://emanual.robotis.com/docs/en/platform/openmanipulator_x/overview/)
### Excute Code
* PC
```
ros2 run test_package real_sub
```
* Raseberry Pi
```
ros2 launch open_manipulator_x_controller open_manipulator_x_controller.launch.py
```

## 3. Station
## 4. RealSense 
## 5. Server

### Feature
- 실내 배송 로봇 서비스에서 배송 정보를 저장하고 관리할 서버(AWS)를 구축 및 스테이션에 저장된 택배를 모니터링하고 배송 완료 시 사용자에게 피드백을 주기 위해 배송 사진 및 시간 로그를 GUI로 표시.

### Main Functions
- MySQL DB
  
  ![address](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/f4fc574a-5a91-462e-b308-543580093d99)

- GUI execute (ROS)
  <pre><code>ros2 run final(pkg_name) my_subscriber(subscribe node py name)</code></pre>


### GUI

  - MySQL DB와 연결하여 업데이트되는 정보(station에 들어온 택배 정보)를 확인.

    ![sql_table](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/1adfa7ff-8c1e-443d-ac24-1caf483bb457)

  - Realsense camera로 촬영된 이미지 확인

    ![gui](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/7721cce2-92dd-496d-ba41-695a0e71dc91)


