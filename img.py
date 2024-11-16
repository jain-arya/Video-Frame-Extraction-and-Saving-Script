import cv2    
import time
cpt = 0
maxFrames = 30

count=0
cap=cv2.VideoCapture('cr.mp4')
while cpt < maxFrames:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 15 != 0:
        continue
    frame=cv2.resize(frame,(1080,500))
    cv2.imshow("test window", frame)
    cv2.imwrite(r"C:\PROGRAMMING\ARYA PYTHON\Crash\image\car_%d.jpg" %cpt, frame)
    cap.get(cv2.CAP_PROP_FPS)
    cpt += 1
    if cv2.waitKey(5)&0xFF==27:
        break
cap.release()   
cv2.destroyAllWindows()