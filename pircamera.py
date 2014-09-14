#!/usr/bin/python3.4

import datetime
import os
import time

import picamera
import RPi.GPIO as GPIO


def get_file_name():
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    return os.path.join("pictures", dt+".jpg")

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam = picamera.PiCamera()

while True:
    time.sleep(.1)
    currState = GPIO.input(sensorPin)
    if currState:  # True if movement, False if no movement
        fileName = get_file_name()
        cam.capture(fileName)
        time.sleep(5)
