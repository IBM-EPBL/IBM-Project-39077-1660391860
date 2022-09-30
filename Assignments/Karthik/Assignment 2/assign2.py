''' 
    Build a python code, Assume u get temperature and humidity values 
    (generated with random function to a variable) and write a condition to continuously 
    detect alarm in case of high temperature.

'''
import random
from time import sleep

temp = 0.0
hum = 0.0


while(True):
    #random values are generated
    temp = random.random()*100
    hum = random.random()*100


    if(temp > 39 and hum < 31 ):
    
        print("Temperature is high")
        print("Temperature : {:.2f} ".format(temp))
        print("Humidity : {:.2f} ".format(hum))
    
    elif(temp < 20 and hum > 50):
       
        print("Temperature is low")
        print("Temperature : {:.2f} ".format(temp))
        print("Humidity : {:.2f} ".format(hum))

    else:   
        print("Reading.......")
    sleep(1)