import numpy as np
import cv2
import pickle
import base64
import json
from threading import Thread
from openalpr import Alpr
import requests


video_feed = cv2.VideoCapture(0)  #'rtsp://admin:admin@192.168.0.176/1'
license_plate_detector = cv2.CascadeClassifier('haar/car_detector.xml')
# car_detector = cv2.CascadeClassifier('haar/car_detector.xml')
# pedestrian_detector = cv2.CascadeClassifier('haar/pedestrian_detector.xml')
# facial_detector = cv2.CascadeClassifier('haar/facial_detector.xml')

def call_aplr_api(b64_jpg):

    base64_image = "data:image/jpeg;base64," + b64_jpg.decode("utf-8")

    URL = "http://localhost:8000/plates"
    HEADERS = { "Content-Type" : "application/json" }
    PARAMS = { "pattern_code": 'no', "country_code": "us", "image": base64_image }
    response = requests.post(url = URL, data = PARAMS)

    print(response.status_code)
    print("Printing Entire Post Request")
    if(len(response.content) > 0):
        print(response.json())

    file1 = open("test.txt", "a")  # append mode
    file1.write(base64_image)
    file1.close()

while(True):
# for x in range(100):
    #Capture frame by frame
    successfull_loop, frame = video_feed.read()

    if successfull_loop:
        greyscale_frame =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    license_plate = license_plate_detector.detectMultiScale(greyscale_frame)
    # cars = car_detector.detectMultiScale(greyscale_frame)
    # pedestrians = pedestrian_detector.detectMultiScale(greyscale_frame)
    # faces = facial_detector.detectMultiScale(greyscale_frame)

    for (x,y,w,h) in license_plate:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
        retval, buffer = cv2.imencode('.jpg', frame)
        b64_jpg = base64.b64encode(buffer)

        thread = Thread(target = call_aplr_api(b64_jpg), args = (10, ))
        thread.start()
        thread.join()

    # for (x,y,w,h) in cars:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # for (x,y,w,h) in pedestrians:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    
    # for (x,y,w,h) in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('computer vision', frame)
    cv2.waitKey(1)

#When everything done, release the capture.
video_feed.release()
cv2.destroyAllWindows()
