import cv2
import numpy as np

img = cv2.imread('face.jpg')
faces_csc = cv2.CascadeClassifier('haarscascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(faces_csc)

faces = faces_csc.detectMultiScale(faces_csc)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,225,0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
