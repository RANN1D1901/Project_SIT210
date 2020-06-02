import cv2
import numpy as np
import os
import time
import RPi.GPIO as GPIO
import threading
from smbus import SMBus
import paho.mqtt.client as mqtt
import smtplib
sender_email='navdeeprandhawa0001@gmail.com'
password='Pass@2019'
def EMAIL():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login(sender_email,password)

    print("Login success")
    message="INTRUDER IN PREMISES"
    print (message)
    server.sendmail(sender_email,sender_email,message)
 
addr = 0x9 # bus address
bus_ = SMBus(1) # indicates /dev/ic2-1
 
def LIGHT():
     bus_.write_byte(addr, 0x1) # switch it on
     time.sleep(10)
     bus_.write_byte(addr, 0x0) # switch it on
 
GPIO.setmode(GPIO.BCM)
pirPIN=26
led=4
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pirPIN,GPIO.IN)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/Desktop/haarcascade_frontalface_default.xml')
cascadePath = "/home/pi/haarcascade_frontalface_default.xml.2"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id = 0
items=['navdeep','intruder']
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)




def MQTT():
    ourClient=mqtt.Client("NAVDEEP_mqtt")
    ourClient.connect("test.mosquitto.org",1883)
    ourClient.publish("argonLOG","ButtonHasBeenPressed")
    ourClient.loop_start()
    while 1:
        time.sleep(1)
def DETECTION():
    while True:
        ret, img =cam.read()
        img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # if confidence is less then 100==> "0" : perfect match 
            if (confidence < 100):
                id = 0
                confidence = "  {0}%".format(round(100 - confidence)) 
            else:
                id = 1
                confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(
                        img, 
                        str(items[id]), 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                       )
            cv2.putText(
                        img, 
                        str(confidence), 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                       )
            if(id==0):
                bus_.write_byte(addr, 0x1) # switch the house led on as the owner is home
                
            if(id==1):
                EMAIL()# the intruder is detected send the mail to the user
        
        cv2.imshow('camera',img) 
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    


def ALARM(pirPIN):
    print("Motion detected")
    t1=threading.Thread(target=MQTT)# this sends signal to the argon(in practical case would be security provider)
    t2=threading.Thread(target=LIGHT)# this turns on the led of the house on for some period of time, this enables camera to work
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
def MOTION():
    GPIO.add_event_detect(pirPIN,GPIO.RISING,callback=ALARM)
    while 1:
        time.sleep(0.2)
t1=threading.Thread(target=DETECTION)
t2=threading.Thread(target=MOTION)
t1.start()
t2.start()
t1.join()
t2.join()
# Do a bit of cleanup
if KeyboardInterrupt:
    print("Exit")
    GPIO.cleanup()
