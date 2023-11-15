ROBOT_DELIVERY
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
![Screenshot from 2023-11-14 18-27-09](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/4b8a4b3b-2843-48c0-ba67-29bd906329db)

# Ros Package
![Screenshot from 2023-11-14 18-26-37](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/7ae18880-0819-4301-9c87-c6da30babded)

# Hardware

## 1. Turtlebot3
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

