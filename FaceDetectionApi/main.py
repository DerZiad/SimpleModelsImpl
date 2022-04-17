import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
i = 0
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        color = (255,0,0)
        stroke = 2
        width = x +  w
        heigth= y + h
        cv2.rectangle(frame,(x,y),(width,heigth),color,stroke)
        savePath = "pictures/" + str(i) + ".png"
        i = i + 1
        cv2.imwrite(savePath,roi_gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()