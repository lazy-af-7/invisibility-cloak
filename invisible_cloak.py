import cv2
import numpy as np

vid=cv2.VideoCapture(0)
back=cv2.imread('./input.jpg')


while vid.isOpened():
    ret,frame=vid.read()

    if ret is True:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv",hsv)
        blue=np.uint8([[[225,0,0]]])
        hsv_blue=cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
        # print(hsv_blue)
        l_blue=np.array([90,100,100])
        u_blue=np.array([130,255,255])
        mask=cv2.inRange(hsv, l_blue, u_blue)
        cv2.imshow("mask",mask)

        temp1=cv2.bitwise_and(back,back,mask=mask)
        mask=cv2.bitwise_not(mask)
        temp2=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('invisibility cloak',temp1+temp2)
        if cv2.waitKey(5) == ord('q'):
            break

vid.release()
cv2.destroyAllWindows()