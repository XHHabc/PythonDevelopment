import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self):
        self.hand_detector = mp.solutions.hands.Hands()  # 获取手势检测器
        self.mpDraw = mp.solutions.drawing_utils
        self.handLmsStyle = self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=5)  # 点的样式
        self.handConStyle = self.mpDraw.DrawingSpec(color=(0, 255, 0), thickness=5)  # 线的样式

    def process(self, img,draw):# 用来画点和线
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # opencv的bgr转成mediapipe需要的rgb
        self.handsData = self.hand_detector.process(img_rgb)
        # print(self.handsData.multi_hand_landmarks)# 侦测到的所有手信息，一个手的信息在landmarkList对象,每个对象有三个数据
        # 三个数据分别是：索引index、判断可信度概率score、关键点坐标

        if draw:
            if self.handsData.multi_hand_landmarks:
                for handLms in self.handsData.multi_hand_landmarks:
                    # 在图片上画出点和线并连接起来
                    self.mpDraw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS, self.handLmsStyle,
                                               self.handConStyle)

    def find_position(self, img):# 用来获取关键点的坐标数据
        h, w, c = img.shape  # 获取画面的高度、宽度、色彩通道
        positions = {'Left': {}, 'Right': {}}
        if self.handsData.multi_hand_landmarks:
            i = 0
            for handPoint in self.handsData.multi_handedness:
                score = handPoint.classification[0].score
                if score >= 0.8:# 可信度
                    label = handPoint.classification[0].label# 标签，表示左右手
                    handLms = self.handsData.multi_hand_landmarks[i].landmark
                    for id, lm in enumerate(handLms):  # id为节点，lm为节点的xyz值
                        x, y = int(lm.x * w), int(lm.y * h)
                        positions[label][id] = (x, y)  # 将获取到的坐标存入字典
                i = i + 1
        return positions


if __name__ == '__main__':
    detector = HandDetector()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()  # 读取摄像头帧
        if not ret:
            break
        if ret:
            frame = cv2.flip(frame, 1)

        # 调用 process 方法进行手势检测并绘制结果
        detector.process(frame, draw=True)

        if detector.handsData.multi_hand_landmarks:
            print(detector.handsData.multi_hand_landmarks)  # 打印手势检测的数据

        cv2.imshow('Hand Detection', frame)

        if cv2.waitKey(1) == 27:  # 'esc' 键退出循环
            break

    cap.release()
    cv2.destroyAllWindows()
