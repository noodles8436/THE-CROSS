# THE-CROSS - Smart Traffic Control Application

- 본 프로젝트는 OSS 개발자 대회 제출용 프로젝트 입니다.

Installation
-----------------------

Before installing, **Install Anaconda on the device you want to run the program on.**

```
conda create -n <env-name> python=3.8
conda activate <env-name>
```
```
pip requirements List
```

Usage
-----------------------
1. Crosswalk & Car Lane Area Setting
   1. At the bottom right of the program screen, find the area you want and click the area setting button.
   2. When clicking the button, wait for the real-time camera image to be displayed in the window window that pops up.
   3. When the real-time camerua image is displayed in the pop-up window window, click four spots on the screen to set a square-shaped area.
   4. If you click more than four spots, the four spots you clicked before will be removed, and you can reset the square-shaped area by clicking the spots again.
   5. To save, press the keyboard "Q" key to save it.

2. How to set the value of time increase or decrease.
   1. Change the several values that exist in the lower left to the desired values. 
   2. Press the "Change Settings" button.

THE-CROSS
--------------------------------------
1. `Images` (Folder)
    - GUI에 사용되는 이미지가 저장되어 있음
2. `customDetector` (Folder)
    - 구급차, 휠체어, 지팡이, 유모차를 인식하는 모델이 저장되어 있음
    - efficientdet_d0_coco17_tpu-32 모델을 Tensorflow Object Detection API를 통해 전이학습 하였음
3. `Camera.py`
    - `VideoThread` : 카메라를 실질적으로 입력 받고 처리하는 클래스
    - `CameraSetup` : 카메라를 설정하는 클래스
4. `FileManager.py`
    - 파일 저장 주소와 초기값이 저장되어있음
    - `configManager` : 파일 입출력 및 저장
5. `ImageDetector.py`
    - `Detector` : Image 배열을 입력받아 보행자가 있다고 예측된 값을 반환하는 메소드
    - `CustomDetector` : Image 배열을 입력받아 [휠체어, 유모차, 지팡이, 구급차] 가 있다고 예측된 값을 반환하는 메소드
6. `ImageUtils.py`
    - `cvImgToQtImg` : OpenCV로 불러온 Image 배열을 QtImg 객체로 반환하는 메소드
    - `resizeCVIMG` : OpenCV로 불러온 Image 배열의 크기를 변경하는 메소드
    - `cvImgToPixmap` : OpenCV로 불러온 Image 배열을 PyQT의 Pixmap 객체로 반환하는 메소드
    - `draw_area` : OpenCV로 불러온 Image 배열과 4개의 꼭짓점을 인수로 받아 Image위에 사각형 영역을 그려서 반환하는 메소드
    - `isSpotInRect` : 4개의 꼭짓점과 특정 점을 인수로 받아 특정 점이 4개의 꼭짓점으로 이루어진 사각형 영역 내에 있는지 반환하는 메소드
7. `SirenDetector.py`
    - `SirenDetector` : 2초 단위로 소리를 입력받아, 해당 소리가 사이렌 소리인지 반환하는 메소드
8. `main.py`
    - `Main` : 프로그램의 중요한 처리를 담당하는 클래스
    - `init` , `initUI` : 프로그램 시작 시, GUI 생성
    - `processing` : Camera.py로 부터 전달 받은 이미지를 처리하여, 신호등을 제어함
    - `TimerMethod` : 신호등 시간을 실질적으로 제어함
