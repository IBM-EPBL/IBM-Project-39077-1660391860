''' Create a raspberry pi python code for simulating a traffic light signal '''

import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

while True: 
    # red 
    GPIO.output(17, True) 
    time.sleep(3)  
    # yellow
    GPIO.output(27, True) 
    time.sleep(2)  
    # green 
    GPIO.output(17, False) 
    GPIO.output(27, False) 
    GPIO.output(11, True) 
    time.sleep(5)  
    # yellow
    GPIO.output(11, False) 
    GPIO.output(27, True) 
    time.sleep(2)  
     
    GPIO.output(10, False)