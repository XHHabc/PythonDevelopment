from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# 手势识别部分
import cv2
import pynput
from .hands_identify import HandDetector

import math
import time
import keyboard
import tkinter as tk



class GesturePage(QWidget):
    def __init__(self, controls):
        super().__init__()
        # 通用全局定义
        self.flag = 1
        self.hand_L = 'Left'
        self.position = None
        self.controls = controls
        self.last_paste_time = 0  # 上一次粘贴操作的时间(用来控制触发频率)
        self.last_doubleClick_time = 0  # 上一次双击操作的时间(用来控制触发频率)

        self.ratioW = None
        self.ratioH = None

        # 创建页面的布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 创建一个用于显示图像的标签
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)  # 将图像标签居中对齐
        layout.addWidget(self.image_label)

        # 创建手势检测器和摄像头捕获对象
        self.hand_detector = HandDetector()
        self.cap = None  # 暂时不打开摄像头

        # 创建定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    # 更新图像帧
    def update_frame(self):
        ret, frame = self.cap.read()  # 从摄像头读取图像
        if ret:
            frame = cv2.flip(frame, 1)  # 水平翻转图像
            self.ratioW, self.ratioH = self.frame_CameraToScreen(frame.shape[1], frame.shape[0])

            ctr = pynput.mouse.Controller()  # 创建鼠标对象
            # self.process_gesture(frame)
            self.test_hands(frame, ctr)
    # 切换启动与关闭=======================================
    def showEvent(self, event):
        super().showEvent(event)
        self.cap = cv2.VideoCapture(0)  # 打开摄像头
        self.timer.start(30)  # 启动定时器

    def hideEvent(self, event):
        super().hideEvent(event)
        self.timer.stop()  # 停止定时器
        if self.cap is not None:
            self.cap.release()  # 释放摄像头资源

    def closeEvent(self, event):
        self.timer.stop()  # 停止定时器
        if self.cap is not None:
            self.cap.release()  # 释放摄像头资源
        event.accept()

    # 手势过程===========================================

    def test_hands(self, img, ctr):
        # 手势键盘========================================================================
        self.hand_detector.process(img, draw=True)
        self.position = self.hand_detector.find_position(img)  # 获取坐标数据

        # 引入八个comboBon控件的值
        port_com101 = self.leftHandPort(int(self.controls['comboBox_101'].currentText()))
        port_com102 = self.leftHandPort(int(self.controls['comboBox_102'].currentText()))

        port_com201 = self.leftHandPort(int(self.controls['comboBox_201'].currentText()))
        port_com202 = self.leftHandPort(int(self.controls['comboBox_202'].currentText()))

        port_com301 = self.leftHandPort(int(self.controls['comboBox_301'].currentText()))
        port_com302 = self.leftHandPort(int(self.controls['comboBox_302'].currentText()))

        port_com401 = self.leftHandPort(int(self.controls['comboBox_401'].currentText()))
        port_com402 = self.leftHandPort(int(self.controls['comboBox_402'].currentText()))

        if port_com102 and port_com202 and port_com302 and port_com402:
            cv2.circle(img, (port_com102[0], port_com102[1]), 7, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (port_com202[0], port_com202[1]), 7, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (port_com302[0], port_com302[1]), 7, (0, 163, 251), cv2.FILLED)
            cv2.circle(img, (port_com402[0], port_com402[1]), 7, (0, 163, 251), cv2.FILLED)

        if port_com101:

            # 复制
            if self.calculate_distance(port_com101, port_com102) <= 10:
                self.fun_copy()

            # 粘贴
            current_time = time.time()  # 获取当前时间
            time_diff = current_time - self.last_paste_time  # 计算与上一次粘贴操作的时间差
            if time_diff >= 1:  # 设置时间间隔为 1 秒
                if self.calculate_distance(port_com201, port_com202) <= 10:
                    self.fun_paste()
                    self.last_paste_time = current_time  # 更新上一次粘贴操作的时间

            # 返回桌面
            if self.calculate_distance(port_com301, port_com302) <= 10:
                self.fun_return_desktop()

            # 截图
            if self.calculate_distance(port_com401, port_com402) <= 10:
                self.fun_screenshot()


        # 手势鼠标========================================================================
        # ctr = pynput.mouse.Controller()  # 创建鼠标对象
        # self.hand_detector.process(img, draw=True)
        # position = self.hand_detector.find_position(img)  # 获取坐标数据
        # 鼠标定位
        mouse_port = self.position[self.hand_L].get(9, None)
        if mouse_port:
            ctr.position = (int(mouse_port[0] * self.ratioW), int(mouse_port[1] * self.ratioH))
            cv2.circle(img, (mouse_port[0], mouse_port[1]), 7, (0,0,0), cv2.FILLED)


        # 鼠标操作
        ltp_8 = self.position[self.hand_L].get(8, None)
        ltp_12 = self.position[self.hand_L].get(12, None)
        ltp_16 = self.position[self.hand_L].get(16, None)

        ltp_4 = self.position[self.hand_L].get(4, None)
        if ltp_8 and ltp_12 and ltp_4 and ltp_16:
            # 关键节点绘画
            cv2.circle(img, (ltp_8[0], ltp_8[1]), 7, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (ltp_12[0], ltp_12[1]), 7, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (ltp_4[0], ltp_4[1]), 7, (0, 255, 255), cv2.FILLED)

            cv2.line(img, (ltp_8[0], ltp_8[1]), (ltp_4[0], ltp_4[1]), (255, 255, 255), 3)  # 食指中指之间的线
            t_1 = int((ltp_4[0] + ltp_8[0]) / 2)
            t_2 = int((ltp_4[1] + ltp_8[1]) / 2)
            cv2.circle(img, (t_1, t_2), 7, (255, 0, 255), cv2.FILLED)  # 食指和中指中间的点

            cv2.line(img, (ltp_12[0], ltp_12[1]), (ltp_16[0], ltp_16[1]), (255, 255, 255), 3)
            t_1 = int((ltp_16[0] + ltp_12[0]) / 2)
            t_2 = int((ltp_16[1] + ltp_12[1]) / 2)
            cv2.circle(img, (t_1, t_2), 7, (255, 0, 255), cv2.FILLED)


            # print(self.calculate_distance(ltp_8, ltp_4))

            if (self.flag == 1) and self.calculate_distance(ltp_8, ltp_12) <= 20:
                current_time = time.time()  # 获取当前时间
                time_diff = current_time - self.last_doubleClick_time  # 计算与上一次粘贴操作的时间差
                if time_diff >= 1:  # 设置时间间隔为 1 秒
                    ctr.click(pynput.mouse.Button.left, 2)  # 模拟鼠标左键双击
                    self.last_doubleClick_time = current_time  # 更新上一次粘贴操作的时间
                self.flag = 0

            if (self.flag == 1) and self.calculate_distance(ltp_4, ltp_8) <= 10:
                ctr.press(pynput.mouse.Button.left)  # 模拟鼠标左键按下操作
                self.flag = 0

            if (self.flag == 0) and self.calculate_distance(ltp_4, ltp_8) > 40:
                ctr.release(pynput.mouse.Button.left)  # 模拟鼠标左键释放操作
                self.flag = 1

            if (self.flag == 1) and self.calculate_distance(ltp_12, ltp_16) <= 10:
                ctr.press(pynput.mouse.Button.right)  # 模拟鼠标右键按下操作
                ctr.release(pynput.mouse.Button.right)  # 模拟鼠标右键释放操作
                self.flag = 0


        # 更新图像标签中的图像
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        qimg = QImage(img_rgb.data, width, height, width * channel, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(qimg))

    def calculate_distance(self, onePort, twoPort):  # 两点之间距离
        distance = math.sqrt((twoPort[0] - onePort[0]) ** 2 + (twoPort[1] - onePort[1]) ** 2)
        return distance

    def leftHandPort(self, num):  # 获取点数据
        port = self.position['Left'].get(num, None)
        return port

    # 手势键盘的四个操作方法
    def fun_copy(self):
        # 模拟按下ctrl+C快捷键
        keyboard.press('ctrl')
        keyboard.press('c')
        time.sleep(0.01)  # 等待一段时间，确保按键生效
        keyboard.release('c')  # 释放
        keyboard.release('ctrl')
        print('执行复制操作')

    def fun_paste(self):
        # 模拟按下ctrl+v快捷键
        keyboard.press('ctrl')
        keyboard.press('v')
        time.sleep(0.01)  # 等待一段时间，确保按键生效
        keyboard.release('v')  # 释放
        keyboard.release('ctrl')
        print('执行粘贴操作')

    def fun_return_desktop(self):  # 返回桌面
        # 模拟按下Win+M快捷键
        keyboard.press('win')
        keyboard.press('m')
        time.sleep(0.01)  # 等待一段时间，确保按键生效
        keyboard.release('m')  # 释放
        keyboard.release('win')
        # keyboard.press('win+m')  # 不可用组合，会使按键不松出现bug

        # # 创建一个线程对象
        # minimize_thread = threading.Thread(target=self.minimize_window)
        # # 启动线程
        # minimize_thread.start()

        # self.showMinimized()  # 最小化当前窗口

    def fun_screenshot(self):  # 截图
        # 模拟按下Win+Shift+s
        keyboard.press('win')
        keyboard.press('shift')
        keyboard.press('s')
        time.sleep(0.01)  # 等待一段时间，确保按键生效
        keyboard.release('s')
        keyboard.release('shift')
        keyboard.release('win')



    def frame_CameraToScreen(self, Cw, Ch):  # 摄像头画面与屏幕画面转换比例
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        return screen_width / Cw, screen_height / Ch




