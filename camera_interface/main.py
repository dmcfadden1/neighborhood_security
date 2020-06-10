import numpy as np
import cv2
import pickle
import requests
import base64
import tkinter as tk
import json
from threading import Thread

# face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')


cap = cv2.VideoCapture(0)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def my_function(b64_jpg):

    base64_image = "data:image/jpeg;base64," + b64_jpg.decode("utf-8")

    URL = 'http://172.31.33.142:4416/plates'
    HEADERS = {'Content-Type' : 'application/json'}
    PARAMS = {'pattern_code': 'no', 'country_code': 'us', 'image': base64_image}
    response = requests.post(url = URL, data = PARAMS)

    print(response.status_code)
    print("Printing Entire Post Request")
    if(len(response.content) > 0):
        print(response.json())

    # file1 = open("test.txt", "a")  # append mode
    # file1.write(base64_image)
    # file1.close()

#while(True):
for x in range(30):
    #Capture frame by frame
    retval, frame = cap.read()

    reduced_frame = rescale_frame(frame, percent=50)


    retval, buffer = cv2.imencode('.jpg', reduced_frame)
    b64_jpg = base64.b64encode(buffer)

    thread = Thread(target = my_function(b64_jpg), args = (10, ))
    thread.start()
    thread.join()


    # for frame in frames:
    #     my_function(frame)



#When everything done, release the capture.
cap.release()
cv2.destroyAllWindows()
