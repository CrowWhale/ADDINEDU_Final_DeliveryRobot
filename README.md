<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Realsense/YOLOv7&fontSize=90"/>


# <div align="center">요약정리</div>

## <div align="center">  🦭 소개 🦭 </div>

<span style="font-size: 10px;"> 실내 배송 로봇 서비스에서 로봇팔로 여러 행위를 하기 위해서는 정확한 위치를 파악하는 것이 필수적이다. 때문에, 절대 좌표계를 기준으로 한, 버튼의 (x,y,z) 좌표를 추출하는 것과 엘리베이터 문과의 거리 측정을 바탕으로 열고 닫았음을 알 수 있도록 RealSense D435 모델과 Yolov7을 활용하여 프로젝트를 진행하였다. </span>

## <div align="center"> 🦄 기술 스택 🦄 </div>

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

## <div align="center"> 🔍 프로그램 실행 🔍 </div>
### (1)
![ezgif com-video-to-gif](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/eb679b0a-1f5f-4909-b294-be70ccbb02f6)
### (2)
![ezgif com-video-to-gif (1)](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/6f97749c-2506-4979-95c4-7861764e332c)



### 카메라 기준 객체 좌표계 추출

## <div align="center"> 🍭 주요 기능 🍭 </div>

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

#### 빌드된 패키지 사용
**Intel® RealSense™ SDK 2.0**은 Ubuntu 16/18/20/22 [LTS](https://wiki.ubuntu.com/LTS)의 Intel X86/AMD64 기반 Debian 배포용으로 [`dpkg`](https://en.wikipedia.org/wiki/Dpkg) 형식의 설치 패키지를 제공합니다. `librealsense2-dkms` 커널 드라이버 패키지는 Ubuntu LTS 커널 4.4, 4.8, 4.10, 4.13, 4.15, 4.18*, 5.0*, 5.3*, 5.4, 5.13 및 5.15를 지원합니다. 자세한 내용은 [Ubuntu 커널 릴리스 일정](https://wiki.ubuntu.com/Kernel/Support)을 참조하십시오.

#### 소스 코드에서 구성 및 빌드
가능한 경우 DKMS 패키지를 사용하는 것이 좋지만 다음 경우에는 수동으로 시스템을 설치하고 패치해야 합니다.
 - LTS가 아닌 Ubuntu 커널 버전 사용: **4.16 **
 - 사용자 지정 패치/모듈을 `librealsense` SDK와 통합.
 - 대안 커널/배포에 대한 패치 조정.

자세한 단계는 [Linux 수동 설치 가이드](./installation.md)에 설명되어 있습니다.

## (1) 패키지 다운로드:
- 서버의 공개 키 등록:
```
sudo mkdir -p /etc/apt/keyrings
curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null
```

- Make sure apt HTTPS support is installed: `sudo apt-get install apt-transport-https`

- 저장소 목록에 서버를 추가: 
```
echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \
sudo tee /etc/apt/sources.list.d/librealsense.list
sudo apt-get update
```

- 라이브러리 설치: 
  `sudo apt-get install librealsense2-dkms`  
  `sudo apt-get install librealsense2-utils`  
위의 두 줄은 librealsense2 udev 규칙을 배포하고 커널 모듈, 런타임 라이브러리, 실행 가능한 데모 및 도구를 빌드 및 활성화합니다.


- 선택적으로 개발자 및 디버그 패키지 설치: 
  `sudo apt-get install librealsense2-dev`  
  `sudo apt-get install librealsense2-dbg`  

Intel RealSense D435 카메라를 다시 연결하고 다음을 실행: `realsense-viewer`

커널 업데이트 확인 :    
`modinfo uvcvideo | grep "version:"` 는 `realsense` 를 포함해야 한다.





## (2) 패키지 업그레이드:
다음을 호출하여 로컬 패키지 캐시를 새로 고칩니다.
  `sudo apt-get update`  

`librealsense` 포함하여 설치된 모든 패키지를 업그레이드합니다.
  `sudo apt-get upgrade`

선택한 패키지를 업그레이드하려면 보다 세부적인 접근 방식만 적용할 수 있습니다.
  `sudo apt-get --only-upgrade install <package1 package2 ...>`  
  예시:   
  `sudo apt-get --only-upgrade install  librealsense2-utils librealsense2-dkms`  

## (3) 패키지 제거:
**Important**  패키지 제거는 설치된 다른 패키지가 이를 직접 참조하지 않는 경우에만 허용된다.
예를 들어,`librealsense2-udev-rules`를 삭제 하기 위해서는 `librealsense2` 를 먼저 지울 것.

다음을 사용하여 단일 패키지를 제거합니다.
  `sudo apt-get purge <package-name>`  

다음을 사용하여 RealSense™ SDK 관련 패키지를 모두 제거하세요.
  `dpkg -l | grep "realsense" | cut -d " " -f 3 | xargs sudo dpkg --purge`  

## 패키지 세부사항:
The packages and their respective content are listed below:  

이름    |      콘텐츠   | Depends on |
-------- | ------------ | ---------------- |
librealsense2-udev-rules | 커널 수준에서 RealSense 장치 권한을 구성합니다.	 | -
librealsense2-dkms | 심도 카메라별 커널 확장용 DKMS 패키지 | librealsense2-udev-rules
librealsense2 | RealSense™ SDK 런타임(.so) 및 구성 파일 | librealsense2-udev-rules
librealsense2-utils | RealSense™ SDK의 일부로 사용 가능한 데모 및 도구	 | librealsense2
librealsense2-dev | 개발자를 위한 헤더 파일 및 심볼릭 링크 | librealsense2
librealsense2-dbg | 개발자를 위한 디버그 기호  | librealsense2
librealsense2-gl | GLSL 확장 모듈 런타임 및 구성 파일 | librealsense2
librealsense2-gl-dev | GLSL 개발 헤더 파일 및 심볼릭 링크 | librealsense2
librealsense2-gl-dbg | 디버깅 목적에 필요한 GLSL 디버그 기호 | librealsense2

<br><br><br><br>


# 2. Official YOLOv7(기초 매뉴얼)

![image](https://github.com/addinedu-ros-2nd/robot-repo-1/assets/47076138/c9a18886-9e22-4fb7-8eeb-6aa1184c149c)


## (1)성능

MS COCO

| Model | 테스트 Size | AP<sup>테스트</sup> | AP<sub>50</sub><sup>테스트</sup> | AP<sub>75</sub><sup>테스트</sup> | 배치 1 fps | 배치 32 average time |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| [**YOLOv7**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) | 640 | **51.4%** | **69.7%** | **55.9%** | 161 *fps* | 2.8 *ms* |
| [**YOLOv7-X**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt) | 640 | **53.1%** | **71.2%** | **57.8%** | 114 *fps* | 4.3 *ms* |
|  |  |  |  |  |  |  |
| [**YOLOv7-W6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6.pt) | 1280 | **54.9%** | **72.6%** | **60.1%** | 84 *fps* | 7.6 *ms* |
| [**YOLOv7-E6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6.pt) | 1280 | **56.0%** | **73.5%** | **61.2%** | 56 *fps* | 12.3 *ms* |
| [**YOLOv7-D6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-d6.pt) | 1280 | **56.6%** | **74.0%** | **61.8%** | 44 *fps* | 15.0 *ms* |
| [**YOLOv7-E6E**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt) | 1280 | **56.8%** | **74.4%** | **62.1%** | 36 *fps* | 18.7 *ms* |

## (2)설치

도커 환경 (추천)
<details><summary> <b>더보기</b> </summary>

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

[`yolov7.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) [`yolov7x.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt) [`yolov7-w6.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6.pt) [`yolov7-e6.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6.pt) [`yolov7-d6.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-d6.pt) [`yolov7-e6e.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt)

``` shell
python test.py --data data/coco.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights yolov7.pt --name yolov7_640_val
```

그 결과는 다음과 같습니다.
```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.51206
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.69730
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.55521
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.35247
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.55937
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.66693
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.38453
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.63765
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.68772
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.53766
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.73549
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.83868
```

정확성 측정을 위해 다음을 다운로드 할것. [COCO-annotations for Pycocotools](http://images.cocodataset.org/annotations/annotations_trainval2017.zip) to the `./coco/annotations/instances_val2017.json`

## (4) 훈련

데이터 준비하기
``` shell
bash scripts/get_coco.sh
```

* MS coco 데이터셋을 다운로드 하세요. ([train](http://images.cocodataset.org/zips/train2017.zip), [val](http://images.cocodataset.org/zips/val2017.zip), [test](http://images.cocodataset.org/zips/test2017.zip)) and [labels](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/coco2017labels-segments.zip). 이전에 다른 버전 YOLO를 사용한 적 있다면 `train2017.cache` and `val2017.cache` 파일을 삭제하고 다시 다운로드 하세요.  [labels](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/coco2017labels-segments.zip) 

'단일' GPU 훈련
``` shell
# train p5 models
python train.py --workers 8 --device 0 --batch-size 32 --data data/coco.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights '' --name yolov7 --hyp data/hyp.scratch.p5.yaml

# train p6 models
python train_aux.py --workers 8 --device 0 --batch-size 16 --data data/coco.yaml --img 1280 1280 --cfg cfg/training/yolov7-w6.yaml --weights '' --name yolov7-w6 --hyp data/hyp.scratch.p6.yaml
```

다중 GPU 훈련
``` shell
# train p5 models
python -m torch.distributed.launch --nproc_per_node 4 --master_port 9527 train.py --workers 8 --device 0,1,2,3 --sync-bn --batch-size 128 --data data/coco.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights '' --name yolov7 --hyp data/hyp.scratch.p5.yaml

# train p6 models
python -m torch.distributed.launch --nproc_per_node 8 --master_port 9527 train_aux.py --workers 8 --device 0,1,2,3,4,5,6,7 --sync-bn --batch-size 128 --data data/coco.yaml --img 1280 1280 --cfg cfg/training/yolov7-w6.yaml --weights '' --name yolov7-w6 --hyp data/hyp.scratch.p6.yaml
```

## (5) 전이 학습

[`yolov7_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt) [`yolov7x_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x_training.pt) [`yolov7-w6_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6_training.pt) [`yolov7-e6_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6_training.pt) [`yolov7-d6_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-d6_training.pt) [`yolov7-e6e_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e_training.pt)

맞춤형 데이터 세트를 위한 단일 GPU 미세 조정
``` shell
# finetune p5 models
python train.py --workers 8 --device 0 --batch-size 32 --data data/custom.yaml --img 640 640 --cfg cfg/training/yolov7-custom.yaml --weights 'yolov7_training.pt' --name yolov7-custom --hyp data/hyp.scratch.custom.yaml

# finetune p6 models
python train_aux.py --workers 8 --device 0 --batch-size 16 --data data/custom.yaml --img 1280 1280 --cfg cfg/training/yolov7-w6-custom.yaml --weights 'yolov7-w6_training.pt' --name yolov7-w6-custom --hyp data/hyp.scratch.custom.yaml
```

## (6) 추론해보기

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
## (1) 

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
해당 코드를 바탕으로, 정면 물체와의 거리를 측정하여, 0.3m 이상이면 엘리베이터 열림, 0.3m이하이면 엘리베이터 닫힘으로 인식한다.

명령어
```
python3 depth_el.py
```
