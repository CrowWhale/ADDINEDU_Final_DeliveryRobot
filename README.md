ROBOT_DELIVERY
====
## INTRODUCTION
### 아파트 내 택배를 자동으로 분류 및 보관하는 Station과 직접 현관 앞까지 배송해주는 배송 로봇 개발
##### Development of a station that automatically sorts and stores apartment packages and a delivery robot that delivers directly to the front door
## DEMO

## 5. Server & GUI part
> - 데이터 관리 서버 (MySQL) / Data Management Server (MySQL)
> - 중앙 관제 및 사용자 피드백 GUI (PyQt, MySQL, ROS) / Central Control and User Feedback GUI (PyQt, MySQL, ROS)


### Introduction
- 실내 배송 로봇 서비스에서 배송 정보를 저장하고 관리할 서버를 구축했다. 또한 스테이션에 저장된 택배를 모니터링하고 배송 완료 시 사용자에게 피드백을 주기 위해 배송 사진 및 시간 로그를 GUI로 나타내었다.

  We built a server to store and manage delivery information in the indoor delivery robot service. In addition, to monitor packages stored at stations and give feedback to users on completion of delivery, delivery photos and time logs were represented as a GUI.


### Environments
-  MySQL, ROS2, PyQT, Python, Vscode, Ubuntu, Github

### Main Functions
- MySQL DB
  
  ![address](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/f4fc574a-5a91-462e-b308-543580093d99)

- GUI execute (ROS)
  <pre><code>ros2 run final(pkg_name) my_subscriber(subscribe node py name)</code></pre>

  ![topic_ros](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/02b3ebd7-11a6-4514-be28-96e1adc7aa61)

  
  ![gui](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/4d3b25ab-2892-43f5-9b0f-1114a48d2852)


### PROCESS
#### 1. Create MySQL DB 
  - DB & TABLES
    
    ![databases](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/951fe891-56e7-46b2-acbf-500926df4a2b)

  - Saved datas
    
    ![address](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/39f156b6-3599-4b0c-9e05-c4c9e53b01de)



#### 2. Create ROS Topic

  - ROS로 토픽이 발행되면(로봇으로부터 배송이 완료되었다고 알림을 받으면) subscribe node를 만들어 PC에 연결된 Realsense depth camera (Intel d435)가 실행되어 촬영하고, GUI로 확인할 수 있게 했다.
      - When a topic is published in ROS (when you receive a notification from the robot that the delivery has been completed), a subscribe node is created to allow the Realsense depth camera (Intel d435) connected to the PC to be executed to shoot and check with the GUI.
    
    ![topic_ros](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/6316bfa1-3e0d-4f4e-b2ee-d5b0af7f4d0c)
  
    ![realsense](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/abd57a2e-3211-41bf-9bd0-ef92ab06952d)
    ![capture](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/11aa01e1-c3c3-47b7-acda-589a6bec1f06)


#### 3. GUI

  - MySQL DB와 연결하여 업데이트되는 정보(station에 들어온 택배 정보)를 확인할 수 있다.
    - You can check the updated information (delivery information entering the station) by connecting to the MySQL DB.

    ![sql_table](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/1adfa7ff-8c1e-443d-ac24-1caf483bb457)

  - Realsense camera로 촬영된 이미지를 볼 수 있다.
    - You can see the images taken with the Realsense camera.
    
    ![gui](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/138747086/7721cce2-92dd-496d-ba41-695a0e71dc91)


  








