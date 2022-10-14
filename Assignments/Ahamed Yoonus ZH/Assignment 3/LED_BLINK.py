'''Create a raspberry pi pythin program to make an led blink '''

import RPi.GPIO as GPIO 
from time import sleep 

 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

while True:
    GPIO.output(22, GPIO.HIGH) 
    sleep(1)
    GPIO.output(22, GPIO.LOW)
    sleep(1) 