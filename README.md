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
======
## 1. 하드웨어

### 입고 part 

- 구현하고자 했던 목표
  - 택배기사님이 택배를 입고하는 부분에 화물을 올려놓는 순간, 택배 정보를 등록, 스테이션에 자동으로 전달
    
- 채택된 아이디어
  - 택배를 레일 특정 구간에 올려놓아서 중간에 정보를 서버에 등록, 마지막에 저장하는 부분에 전달하게 하자.

레일 사진

#### 결과
> * PIR 적외선 센서를 두개 사용해서 각각 택배를 올려놓는 순간이랑 택배 정보를 저장하는 순간을 감지한다
> * 카메라로 택배사진을 찍을때를, 택배 정보를 저장하는 순간으로 설정하자



### 스테이션 part

- 구현하고자 했던 목표
  - 공간 효율화
  - 출고 순서를 조절
  - 기존 유사 아이디어들과 차별화
    
- 채택된 아이디어
  - 관람차처럼 회전, 순환하면서 택배를 저장하는 구조를 구현하자.

기구학적인 구조 설명하는 사진
조건1: 택배를 저장, 출고, 바구니를 회전하는 그 어떤 상황에서든 바구니의 평형을 유지해야한다.
조건2: 바구니의 진행경로상에서 다른 바구니와의 충돌 즉 다른 바구니의 회전을 막아서는 안된다.

스테이션 저장부분 사진

##### 결과
> * 바구니의 평형을 유지하기위해 축 바구니 양쪽 옆에 바구니를 지지해주는 축을 각각 하나 총 두개를 사용
> * 바구니가 움직이는 경로를 레일로 구현, 레일 두개를 바구니 양옆으로 바구니 축이랑 결합할수 있게 함

## 2. 소프트웨어

아두이노로 코드를 짜서 





  
