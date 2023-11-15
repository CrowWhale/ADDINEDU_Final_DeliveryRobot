ROBOT_DELIVERY
=========
Introduction
=========
### 아파트 내 택배를 자동으로 분류 및 보관하는 STATION과 현관까지 배공해주는 배송 주행 로봇 개발
# Demo
dddddddddddddddddddd
# Sequence
1. 자율주행 part
> * 배송로봇 자율주행 구현(ROS, Mapping, Navigation)
2. Manipulator
> * manipulator 구동 알고리즘(ROS)
> * 이송 객체 크기 인식(Deep Learning, Computer Vision)
3. Station part
> * Station 제작 및 구동 알고리즘(3D modeling & printing, IoT)
4. Computer Vision & 영상처리 part
> * 객체 text 데이터 인식(Computer vision, Image processing)
# Environments
<div align="center">
  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/c5d1ed7c-905f-48e6-a4e4-0cad3d4f0f35" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/a8c8ff1d-4b09-4ee2-997a-39cebda308e8" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/5f791e00-8687-4b88-ae2a-63cf7c4d0fa8" width="15%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

  <a>
    <img src="https://github.com/addinedu-ros-2nd/robot-repo-1/assets/132206474/31c6515f-a85c-4e3b-bfeb-5d5ee8533792" width="7%" /></a> 
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
  <a>
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-docker-small.png" width="7%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
  <a>
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-aws-small.png" width="7%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />

</div>

# Station

# 1. STATION 하드웨어

## INPUT PART : 택배기사가 택배를 올려놓는 곳
  
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

## STATION PART : 택배가 규칙에 맞게 저장되는 곳
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

## FINAL PRODUCT
 
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

# 2. Station 소프트웨어

구성한 하드웨어를 다루기 위해 선택한 수단은 아두이노랑 ROS2다. 아두이노를 통해 센서들의 정보를 처리하면서 모터 두개를 제어하고, 택배 정보를 입력하는 수단인 카메라랑 정보를 주고 받기 위해 ROS2를 사용했다.


 <pre><code>
   // 아두이노로부터 정보를 받아와 subscriber에게 정보를 발행하는 publisher 실행코드
   ros2 run arduino_station arduino_publisher --ros-args --params-file ~/final_ws/src/arduino_station/param/arduino_config.yaml
 </code></pre>

 
<pre><code>
  // publisher로부터 정보를 받아 카메라를 실행하고 층 수 정보를 아두이노에게 전달하는 subscriber 실행코드 
  ros2 run arduino_station arduino_subscriber --ros-args --params-file ~/final_ws/src/arduino_station/param/arduino_config.yaml
</code></pre>











  
