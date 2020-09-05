#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

in1 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)   

time.sleep(0.25)
GPIO.output(in1, GPIO.HIGH)

time.sleep(1)

GPIO.output(in1, GPIO.LOW)   

GPIO.cleanup()
