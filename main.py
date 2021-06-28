import cv2
vid=cv2.VideoCapture(0)

while vid.isOpened():
     ret, back = vid.read()
     
     if ret==True:
         cv2.imshow("input",back)
         if cv2.waitKey(5) == ord('q'):
             cv2.imwrite('input.jpg',back)
             break
vid.release()
cv2.destroyAllWindows()

