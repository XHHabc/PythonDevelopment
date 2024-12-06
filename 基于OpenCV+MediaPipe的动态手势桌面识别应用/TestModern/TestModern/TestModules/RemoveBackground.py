import cv2

cap = cv2.VideoCapture(0)
mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if ret:
        mask = mog.apply(frame)
        cv2.imshow('video', mask)

    key = cv2.waitKey(1)
    if key == 27:  # 按Esc退出
        break

cap.release()
cv2.destroyAllWindows()
