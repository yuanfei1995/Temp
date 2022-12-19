#coding:utf8
import cv2
import dlib
import numpy as np
import sys
import os

cascade_path='haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)

images = os.listdir(sys.argv[1])
for image in images:
    im=cv2.imread(os.path.join(sys.argv[1],image),1)
    rects = cascade.detectMultiScale(im, 1.3,5)
    print "detected face",len(rects)
    if len(rects) == 0:
        #cv2.namedWindow('Result',0)
        #cv2.imshow('Result',im)
        #k =cv2.waitKey(0)
        os.remove(os.path.join(sys.argv[1],image))
        #if k == ord('q'):
            #break

