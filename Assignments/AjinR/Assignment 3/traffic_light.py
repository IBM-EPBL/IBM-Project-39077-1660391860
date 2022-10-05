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
    GPIO.output(9, True) 
    time.sleep(3)  
    # yellow
    GPIO.output(10, True) 
    time.sleep(2)  
    # green 
    GPIO.output(9, False) 
    GPIO.output(10, False) 
    GPIO.output(11, True) 
    time.sleep(5)  
    # yellow
    GPIO.output(11, False) 
    GPIO.output(10, True) 
    time.sleep(2)  
     
    GPIO.output(10, False)