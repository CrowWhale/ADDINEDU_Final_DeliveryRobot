<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Realsense/YOLOv7&fontSize=90"/>


# <div align="center">요약정리</div>

## <div align="center">  소개 </div>

<span style="font-size: 10px;"> 실내 배송 로봇 서비스에서 로봇팔로 여러 행위를 하기 위해서는 정확한 위치를 파악하는 것이 필수적이다. 때문에, 절대 좌표계를 기준으로 한, 버튼의 (x,y,z) 좌표를 추출하는 것과 엘리베이터 문과의 거리 측정을 바탕으로 열고 닫았음을 알 수 있도록 RealSense D435 모델과 Yolov7을 활용하여 프로젝트를 진행하였다. </span>

## <div align="center"> 기술 스택 </div>

<div align="center">
	<img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white" />
	<img src="https://img.shields.io/badge/mysql-4479A1?style=flat&logo=mysql&logoColor=white" />
	<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white" />
	<img src="https://img.shields.io/badge/visual studio code-007ACC?style=flat&logo=visualstudiocode&logoColor=white" />
	<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=C%2B%2B&logoColor=white"/>
 	<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/>
  	<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
   	<img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=Ubuntu&logoColor=white"/>
</div>

## <div align="center"> 프로그램 실행 </div>
### (1) 로봇 기준, 인식된 객체의 좌표계 추출
![ezgif com-video-to-gif](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/eb679b0a-1f5f-4909-b294-be70ccbb02f6)
### (2) 로봇 기준 정면 물체(엘리베이터)와의 거리 실시간 검출
![ezgif com-video-to-gif (1)](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/6f97749c-2506-4979-95c4-7861764e332c)



## <div align="center"> 주요 기능 </div>

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


# 1. RealSense SDK(기초 매뉴얼 )


## (1) 패키지 다운로드:
- 서버의 공개 키 등록:
```
sudo mkdir -p /etc/apt/keyrings
curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null
```

`sudo apt-get install apt-transport-https`

- 저장소 목록에 서버를 추가: 
```
echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \
sudo tee /etc/apt/sources.list.d/librealsense.list
sudo apt-get update
```

- 라이브러리 설치: 
  `sudo apt-get install librealsense2-dkms`  
  `sudo apt-get install librealsense2-utils`  

- 선택적으로 개발자 및 디버그 패키지 설치: 
  `sudo apt-get install librealsense2-dev`  
  `sudo apt-get install librealsense2-dbg`  

Intel RealSense D435 카메라를 다시 연결하고 다음을 실행: `realsense-viewer`

커널 업데이트 확인 :    
`modinfo uvcvideo | grep "version:"` 는 `realsense` 를 포함해야 한다.





## (2) 패키지 업그레이드:
  `sudo apt-get update`  

`librealsense` 포함하여 설치된 모든 패키지를 업그레이드
  `sudo apt-get upgrade`

선택한 패키지를 업그레이드하려면 보다 세부적인 접근 방식
  `sudo apt-get --only-upgrade install <package1 package2 ...>`  
  예시:   
  `sudo apt-get --only-upgrade install  librealsense2-utils librealsense2-dkms`  

## (3) 패키지 제거:

다음을 사용하여 단일 패키지를 제거
  `sudo apt-get purge <package-name>`  

다음을 사용하여 RealSense™ SDK 관련 패키지를 모두 제거
  `dpkg -l | grep "realsense" | cut -d " " -f 3 | xargs sudo dpkg --purge`  


# 2. Official YOLOv7(기초 매뉴얼)

## (1)성능

MS COCO

| Model | 테스트 Size | AP<sup>테스트</sup> | AP<sub>50</sub><sup>테스트</sup> | AP<sub>75</sub><sup>테스트</sup> | 배치 1 fps | 배치 32 average time |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| [**YOLOv7**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) | 640 | **51.4%** | **69.7%** | **55.9%** | 161 *fps* | 2.8 *ms* |
| [**YOLOv7-X**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt) | 640 | **53.1%** | **71.2%** | **57.8%** | 114 *fps* | 4.3 *ms* |

## (2)설치

``` shell
# create the docker container, you can change the share memory size if you have more.
nvidia-docker run --name yolov7 -it -v your_coco_path/:/coco/ -v your_code_path/:/yolov7 --shm-size=64g nvcr.io/nvidia/pytorch:21.08-py3

# apt install required packages
apt update
apt install -y zip htop screen libgl1-mesa-glx

# pip install required packages
pip install seaborn thop

# go to code folder
cd /yolov7
```

</details>

## (3) 테스트

[`yolov7.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) [`yolov7x.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt)
``` shell
python test.py --data data/coco.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights yolov7.pt --name yolov7_640_val
```
## (4) 훈련

데이터 준비
``` shell
bash scripts/get_coco.sh
```

'단일' GPU 훈련
``` shell
# train p5 models
python train.py --workers 8 --device 0 --batch-size 32 --data data/coco.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights '' --name yolov7 --hyp data/hyp.scratch.p5.yaml

# train p6 models
python train_aux.py --workers 8 --device 0 --batch-size 16 --data data/coco.yaml --img 1280 1280 --cfg cfg/training/yolov7-w6.yaml --weights '' --name yolov7-w6 --hyp data/hyp.scratch.p6.yaml
```

## (5) 전이 학습

[`yolov7_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt) [`yolov7x_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x_training.pt)


## (6) 추론

비디오 :
``` shell
python detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source yourvideo.mp4
```

이미지 :
``` shell
python detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source inference/images/horses.jpg
```

![image](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/811e1317-de4e-4b8e-97e3-ef6e7227cccc)



<br><br><br><br>

# 3. YOLOv7 학습된 데이터와 RealSense D435를 활용한 좌표 추출

detect_RS.py 코드 중 일부...
```
--- 생략 ---
        if key == ord('p'):
            # 'p' 키를 눌렀을 때의 동작
            with open("pixel_data.txt", "w") as file:
                for label, (depth_point_in_color[0], depth_point_in_color[1], depth_point_in_color[2]) in depth_info.items():
                    file.write(f'{label}: {depth_point_in_color[0]:.5f},{depth_point_in_color[1]:.5f},{depth_point_in_color[2]:.5f}\n')
        if key == ord('q'):
            break
--- 이하 생략 ---
```
해당 코드를 바탕으로, 객체 인식된 각각의 요소의 x,y,z 좌표를 pixel_data.txt 텍스트 파일에 저장한다.

명령어
```
python3 detect_RS.py --weights [학습모델] --conf-thres [원하는 확률]
```
예시)
```
python3 detect_RS.py --weights best.pt --conf-thres 0.5
```

# 4. Realsense D435를 활용한 정면 물체와의 거리 측정

depth_el.py 코드 중 일부...
```
--- 생략 ---
                x, y = 320, 240
                depth_el = round(depth_frame.get_distance(x, y), 2)
                print("엘리베이터와의 거리: ", depth_el, "m")
​
                if depth_el >= 0.3 :
                    print("엘리베이터 열림")
                    self.toggle = 1  # 거리가 30 이상이면 toggle에 1 저장
                else:
                    # print("엘리베이터 닫힘")
                    self.toggle = 0  # 거리가 30 미만이면 toggle에 0 저장
​
                color_image = np.asanyarray(aligned_frames.get_color_frame().get_data())
                cv2.imshow('RealSense', cv2.circle(color_image, (x, y), 2, (0, 0, 255), -1))
--- 이하 생략 ---
```
<br>
해당 코드를 바탕으로, 정면 물체와의 거리를 측정하여, 0.3m 이상이면 엘리베이터 열림, 0.3m이하이면 엘리베이터 닫힘으로 인식한다.

명령어
```
python3 depth_el.py
```
