import cv2 as cv
import numpy as np
# facial recognition done thorugh classifiers
# Haar cascade --> pre-trained classifier
# A classifier is an algorithm that deceides whether an image is positive or negative
# positive image --> one containing an object that must be detected 
# negative image --> one not containing a need-to-find object
# opencv harcascade library --> https://github.com/opencv/opencv/tree/master/data/haarcascades
# Stack Overflow post --> https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
# https://maelfabien.github.io/tutorials/face-detection/#



face_cascade=cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade=cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_eye_tree_eyeglasses.xml")
smile_cascade=cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_smile.xml")

cap=cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    grey=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.05,5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        roi_grey=grey[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_grey,1.05,5)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),3) 
        smile=smile_cascade.detectMultiScale(roi_grey,1.05,5)
        for (sx,sy,sw,sh) in smile:
            cv.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),3)
    cv.putText(frame,"Face",(20,40),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(0,255,0),thickness=3)
    cv.putText(frame,"Eyes",(20,80),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(255,0,0),thickness=3)
    cv.putText(frame,"Lips",(20,120),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(0,0,255),thickness=3)
    cv.imshow("Live",frame)
    if cv.waitKey(1) == ord('q'):
        break