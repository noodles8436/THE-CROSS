import numpy as np
import cv2
import DetectorConnector

from PyQt5.QtCore import QThread, pyqtSignal
from ImageUtils import draw_area

IMAGE_PATH = "Images/"
DETECTOR_SERVER_IP = 'localhost'
DETECTOR_SERVER_PORT = 7777


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray, np.ndarray, list, list, list, list)

    def __init__(self, left_camera_num, right_camera_num):
        super().__init__()
        self._run_flag = True
        self.left_camera_num = left_camera_num
        self.right_camera_num = right_camera_num
        self.conn = DetectorConnector.Connector(DETECTOR_SERVER_IP, DETECTOR_SERVER_PORT)

    def setCameraNumber(self, left_num, right_num):
        self.left_camera_num = left_num
        self.right_camera_num = right_num

    def isRun(self):
        return self._run_flag

    def run(self):
        # capture from web cam
        cam_left = cv2.VideoCapture(self.left_camera_num)
        cam_right = cv2.VideoCapture(self.right_camera_num)

        self._run_flag = True

        while self._run_flag:
            ret_left, cv_img_left = cam_left.read()
            ret_right, cv_img_right = cam_right.read()

            pos_left = []
            pos_right = []
            custom_pos_left = [[], [], [], []]
            custom_pos_right = [[], [], [], []]

            if ret_left is False:
                img_result_left = np.array([])
            else:
                img_result_left = cv_img_left
                result = self.conn.processing(cv_img_left)
                if result is not None:
                    pos_left = result[0]
                    if len(custom_pos_left) != 0:
                        custom_pos_left = result[1]

            if ret_right is False:
                img_result_right = np.array([])
            else:
                img_result_right = cv_img_right
                result = self.conn.processing(cv_img_right)
                if result is not None:
                    pos_right = result[0]
                    if len(custom_pos_right) != 0:
                        custom_pos_right = result[1]

            # Emit Lists To Main Processing Method
            self.change_pixmap_signal.emit(img_result_left, img_result_right,
                                           pos_left, pos_right, custom_pos_left, custom_pos_right)

        # shut down capture system
        cam_left.release()
        cam_right.release()

    def stop(self):
        self._run_flag = False

    def close(self):
        self.stop()
        self.conn.disconnect()
        self.exit()


class CameraSetup:

    def __init__(self, camera_num):
        super().__init__()
        self.touch_list = []
        self.windowName = 'Camera Setup :: Save & Exit Button is KEY Q'
        self.isRun = True
        self.Camera_Number = camera_num
        self.CAMERA_NO_SIGNAL_IMG = cv2.imread(IMAGE_PATH + "camera_no_signal.png")

    def addXY_inList(self, x, y):
        if len(self.touch_list) >= 4:
            self.touch_list = []
        self.touch_list.append([x, y])

    def clear_List(self):
        self.touch_list = []

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print('x : ', x, ' y : ', y)
            self.addXY_inList(x, y)

    def runSetup(self):
        cv2.namedWindow(self.windowName)
        cv2.setMouseCallback(self.windowName, self.click_event)

        cap = cv2.VideoCapture(self.Camera_Number)

        while self.isRun:
            ret, frame = cap.read()
            if ret is False:
                frame = self.CAMERA_NO_SIGNAL_IMG
            else:
                frame = draw_area(frame, self.touch_list)

            cv2.imshow(self.windowName, frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key & 0xFF == ord('Q'):
                self.isRun = False
                cv2.destroyWindow(self.windowName)
                cap.release()
                cv2.waitKey(10)
                return self.touch_list
