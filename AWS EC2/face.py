#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import glob
import random
import sys

emotions = ["neutrality", "anger", "fear", "happiness", "sadness", "surprise"]
fishface = cv2.createFisherFaceRecognizer() 
#eigenface = cv2.createEigenFaceRecognizer()
#LBPface = cv2.createLBPHFaceRecognizer()

def detect_target_faces():
    flag = 0
    face_img = cv2.imread('/var/www/html/face.jpg') 
    face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    face_gray = clahe.apply(face_gray)
    faceDet = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faceDet2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    faceDet3 = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    faceDet4 = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
    face = faceDet.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    face2 = faceDet2.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    face3 = faceDet3.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    face4 = faceDet4.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(face) == 1:
        facefeature = face
    elif len(face2) == 1:
        facefeature = face2
    elif len(face3) == 1:
        facefeature = face3
    elif len(face4) == 1:
        facefeature = face4
    else:
        print('Sorry, no face detected!')
        flag = 1
        facefeature = ''
    for (x, y, w, h) in facefeature: 
        cut = face_gray[y:y+h, x:x+w]
        try:
            extr_face = cv2.resize(cut, (350, 350))
            #cv2.imwrite("face_extracted.jpg", extr_face)
            flag = 0
            return flag, extr_face
        except:
            return flag, extr_face

def aaaa():
    flag, face = detect_target_faces()
    if(flag==0): 
        face_gray = face
        fishface.load('/var/www/html/fishface_mode.XML')
        res_index = fishface.predict(face_gray)
        u=res_index[0]
        res_exp1 = emotions[u]
    print(res_exp1)
    return res_exp1

if __name__ == '__main__':
    aaaa()
