# THE-CROSS - Smart Traffic Control Application

- This project is for submitting the OSS Developer Competition.

Installation
-----------------------

Before installing, Please check the two points below.   
1. **Install Anaconda on the device you want to run the program on.**   
2. **Make sure at least one camera is connected on the device**   
( WebCam and USB CAM are both available, but I recommend using USB CAM. )   

   
Open command prompt and create conda environment
```
conda create -n <env-name> python=3.8
conda activate <env-name>


:: CONDA EXAMPLE ::
conda create -n cross python=3.8
conda activate cross
```

Then, Download Project from github, Open Conda prompt ***in Project Folder*** and   
Follow commands below **TO DOWNLOAD DETECITON MODEL**
```
git clone https://github.com/noodles8436/THE-CROSS.git

cd THE-CROSS

pip install -r requirements.txt
python download_model.py
```

Usage
-----------------------

 1. ### Open Image Detection Server   
    Follow the below command to open Image Detection Server   
    :: CAUTION :: ***wait until "Socket Opened" Message printed***
    ```
    python DetectorServer.py
    ```
 2. ### Open Client Program
    Open ***new Conda Prompt in Project Folder ( activated `<env-name>` )*** and Follow below command **TO OPEN CLIENT PROGRAM**
    ```
    conda activate <env-name>
    cd THE-CROSS
    
    python main.py
    ```
   
3. ### Setting Crosswalk & Car Lane Area
   1. At the bottom right of the program screen, find the area you want and click the area setting button.
   2. When clicking the button, wait for the real-time camera image to be displayed in the window window that pops up.
   3. When the real-time camerua image is displayed in the pop-up window window, click four spots on the screen to set a square-shaped area.
   4. If you click more than four spots, the four spots you clicked before will be removed, and you can reset the square-shaped area by clicking the spots again.
   5. To save, press the keyboard "Q" key to save it.

4. ### Setting the value of time increase or decrease.
   1. Change the several values that exist in the lower left to the desired values. 
   2. Press the "Change Settings" button.

FAQ
----------------------

Library License
----------------------
```
tensorflow = Apache 2.0   
tensorflow-hub = Apache 2.0   
OpenCV = Apache 2.0   
PyQT5 = GPL v3   
Numpy = BSD 3-Clause   
sounddevice = MIT   
gdown = MIT   
```

How to Conribute
----------------------

Contributors
----------------------
