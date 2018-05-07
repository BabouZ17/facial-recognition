#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Little demo script for eyes and faces recognitions using faces cascade Classifier#
"""
Little demo to capture eyes and faces from a video feed and faces cascade Classifier
"""

from os import path

import cv2
import numpy as np

path_to_classifier = '/usr/local/lib/python3.6/dist-packages/cv2/data/'
faces_classifier_path = 'haarcascade_frontalface_default.xml'
eyes_classifier_path = 'haarcascade_eye.xml'

faces_classifier = cv2.CascadeClassifier(path.join(path_to_classifier, faces_classifier_path))
eyes_classifier = cv2.CascadeClassifier(path.join(path_to_classifier, eyes_classifier_path))

feed = cv2.VideoCapture(0)
feed.set(3, 1980) # Width
feed.set(4, 1024) # Height

while 1:
    # Get the frame
    ret, frame = feed.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faces_classifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyes_classifier.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255, 0, 255), 2)

    # Show the frame
    cv2.imshow('Live Feed', frame)

    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

feed.release()
cv2.destroyAllWindows()
