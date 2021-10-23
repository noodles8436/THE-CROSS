# THE-CROSS - Smart Traffic Control Application

- This project is for submitting the OSS Developer Competition.

Installation
-----------------------

Before installing, Please check the two points below.   
1. **Install Anaconda on the device you want to run the program on.**   
2. **Make sure at least one camera is connected on the device**

   
Open command prompt and create conda environment
```
conda create -n <env-name> python=3.8
conda activate <env-name>
```

Then, Download Project from github, Open Conda prompt ***in Project Folder*** and Follow commands below
```
pip install -r requirements.txt
python setup.py
```

Next, Follow command below to open Image Detection Server   
:: CAUTION :: ***wait "Socket Opened" Message***
```
python DetectorServer.py
```

Finally, Open ***new Conda Prompt in Project Folder ( activated `<env-name>` )*** and follow below command
```
python main.py
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

FAQ
----------------------

License
----------------------

How to Conribute
----------------------

Contributors
----------------------
