
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/1d1ae5ba-0597-4bc5-b567-6f2b2752250f" width="60%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />



<div align="center">
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/1a0dfe7d-cfb7-47bd-9533-50f22116c066" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/e9cf6aa9-caf8-400a-9595-52d9b8c6d868" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/b09747e0-9062-4c11-837a-8d5476ee8935" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/a60b8991-157c-46c1-8c81-04633c1a5467" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/3d8f2193-f36c-4197-b07a-2ff332a9a36f" width="7%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
  <a>
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-docker-small.png" width="7%" /></a>

</div>

Introduction
=========
### 아파트 내 택배를 자동으로 분류 및 보관하는 STATION과 현관까지 배송해주는 DELIVERY_ROBOT 개발
# Demo
<div align="center">
  <img src="gif/demo.gif"/>
</div>

[『YOUTUBE_FULL_DEMO_VIDEO』](https://www.youtube.com/watch?v=yonJqRplI4o)

# SYSTEM_CONFIGURATION
![Screenshot from 2023-11-14 17-40-37](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/c881aef8-e224-4ff2-b445-d4ea391d142d)
1. 자율주행 part
* 배송로봇 자율주행 구현(ROS, Mapping, Navigation)
2. Manipulator
* manipulator 구동 알고리즘(ROS)
* 이송 객체 크기 인식(Deep Learning, Computer Vision)
3. Station part
* Station 제작 및 구동 알고리즘(3D modeling & printing, IoT)
4. Computer Vision & 영상처리 part
* 객체 text 데이터 인식(Computer vision, Image processing)

# TOTAL_SEQUENCE
![왕빵스케치시퀀스](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/1c8ca792-1681-4096-b700-53bde99febdb)

# Software Design
## 1. 배달리오 시스템 상태전이도
![스테이션](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/12d164d9-4c28-4b72-8314-7c2df1d446bc)
## 2. 아파트 내 엘리베이터 도착 및 탑승
![엘리베이터](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/595b23e2-877f-4102-b54b-fe6e8f4648d6)
## 3. 현관 배송 후 복귀
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
### INPUT PART : 택배기사가 택배를 올려놓는 곳
  
| TITLE | Input Part |
|:---:|:-----------------------|
| GOAL | <br>- 택배기사님이 택배를 올려놓는 순간 이후 정보 등록, 스테이션 전달 자동화 <br><br> |
| IDEA | <br>- 택배를 레일 시작 구간에 올려놓아 중간에 정보를 서버에 등록, 마지막에 Station에 전달하자 <br><br> |
| RESULT | <br>- PIR 적외선 센서를 두개 사용 <br> - 각각 택배를 올려놓는 순간이랑 정보를 저장하는 순간을 감지 <br> - 정보를 저장할때 카메라 사용 <br><br> |

<div align="center">
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/dcff9c37-9f38-49cc-872f-e5e4adbc7f57" width="20%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

<a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/3c4696ca-144e-4edf-9bf6-c5ce3bf0b5e5" width="20%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  </div>

***

### STATION PART : 택배가 규칙에 맞게 저장되는 곳
| TITLE |  Station Part |
|:---:|:----------------------|
| GOAL | <br>- 공간효율화 <br> - 출고 순서를 마음대로 조절 <br> - 기존 유사 아이디어들과 차별화<br><br>|
| IDEA | <br>- 관람차처럼 회전, 순환하면서 택배를 저장하는 구조를 구현하자 <br><br>|
| DETAIL | <br>- 택배를 저장, 출고, 바구니를 회전하는 그 어떤 상황에서든 바구니의 평형을 유지해야한다. <br> - 바구니의 진행경로상에서 다른 바구니와의 충돌 즉 다른 바구니의 회전을 막아서는 안된다. <br> <br>|
| RESULT | <br>- 바구니의 평형을 유지하기위해 축 바구니 양쪽 옆에 바구니를 지지해주는 축을 각각 하나 총 두개를 사용 <br> - 바구니가 움직이는 경로를 레일로 구현, 레일 두개를 바구니 양옆으로 바구니 축이랑 결합할수 있게함 <br> - 뼈대와 레일 구조는 과학상자6호를 사용해서 구현했으며, 바구니는 직접 3D 모델링을 해서 설계했다. <br><br>|

<div align="center">
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/ba506897-1435-4688-b4a1-dcf31c32a36a" width="20%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/74ddc5f0-5b8a-4d89-9295-5c3cc4e814eb" width="20%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/b32db026-1fdc-400c-884c-a8378d228212" width="20%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/aa3a01b7-b49f-45b4-8b51-16ffe0ca75d8" width="20%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
</div>

***

### FINAL PRODUCT
 
<div align="center">
  
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/03fed296-cf10-4c82-a99c-f4d7c3eaa8dc" width="20%"/></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/efb97d7e-ac65-4343-9d41-62740af63a02" width="15%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/140477483/8d4480f1-d2a6-480e-96a2-983f2098f294" width="20%"/></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
    
</div>




#### 주요 구성품
> * 과학상자 6호
> * PIR 센서 두개
> * 초음파 센서
> * DC 모터
> * 엔코더장착형 감속기어모터 IG-28GM+Encoder 01 TYPE
> * L298n 모터드라이버
***

### Excute Code

아두이노를 통해 센서들의 정보를 처리하면서 모터 두개를 제어하고, 택배 정보를 입력하는 수단인 카메라랑 정보를 주고 받기 위해 ROS2를 사용

* 아두이노로부터 정보를 받아와 subscriber에게 정보를 발행하는 publisher 실행코드
 <pre><code>
   ros2 run arduino_station arduino_publisher --ros-args --params-file ~/final_ws/src/arduino_station/param/arduino_config.yaml
 </code></pre>

* publisher로부터 정보를 받아 카메라를 실행하고 층 수 정보를 아두이노에게 전달하는 subscriber 실행코드 
<pre><code>
  ros2 run arduino_station arduino_subscriber --ros-args --params-file ~/final_ws/src/arduino_station/param/arduino_config.yaml
</code></pre>

## 4. RealSense 
### Feature
- 실내 배송 로봇 서비스에서 로봇팔로 여러 행위를 하기 위해서는 정확한 위치를 파악하는 것이 필수이므로 절대 좌표계를 기준으로 한, 버튼의 (x,y,z) 좌표를 추출하는 것과 엘리베이터 문과의 거리 측정을 바탕으로 열고 닫았음을 알 수 있도록 RealSense D435 모델과 Yolov7을 활용하여 프로젝트를 진행

- 카메라 기준 절대 좌표계에서 인식한 객체의 좌표를 추출하여 텍스트 파일로 저장하는 명령어

```
python3 detect_RS.py --weights yolov7.pt --conf-thres 0.2

```
![image](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/f43497bb-643e-4a73-9224-b77bd7972e11)

- 엘리베이터까지의 거리값을 인식하여 0.3m 이상일 경우 엘리베이터 문이 열림, 0.3m 이하일 경우 엘리베이터 문이 닫힘으로 인식하는 명령어
  
```
python3 depth_el.py
```
![ezgif com-video-to-gif (1)](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/8f41da90-46bc-4bc0-a9a1-62c78b1b427c)

* Trained Model 
[`yolov7_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt) [`yolov7x_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x_training.pt)

### Excute Code
* PC
```
ros2 run depth_example mail_node.py
```
<div align="center">
  <img src="gif/detect_push.gif"/>
</div>

## 5. Server

### Feature
- 실내 배송 로봇 서비스에서 배송 정보를 저장하고 관리할 서버(AWS)를 구축 및 스테이션에 저장된 택배를 모니터링하고 배송 완료 시 사용자에게 피드백을 주기 위해 배송 사진 및 시간 로그를 GUI로 표시.
- 가상 server를 생성 및 대시보드로 소포의 주소를 간략히 확인 

### Main Functions
- MySQL DB
  
  ![address](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/f4fc574a-5a91-462e-b308-543580093d99)

- GUI execute (ROS)
  <pre><code>ros2 run final(pkg_name) my_subscriber(subscribe node py name)</code></pre>

- Metabase
    <pre><code>docker start metabase</code></pre>


### GUI

  - MySQL DB와 연결하여 업데이트되는 정보(station에 들어온 택배 정보)를 확인.

    ![sql_table](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/1adfa7ff-8c1e-443d-ac24-1caf483bb457)

  - Realsense camera로 촬영된 이미지 확인

    ![gui](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/7721cce2-92dd-496d-ba41-695a0e71dc91)

### Metabase
  - MySQL DB와 연결한 Metabase에 대시보드로 실시간 주소 정보 확인
      ![sql_with_dashboard](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/d874e2ad-0c10-4304-9566-7988b4e7a220)

