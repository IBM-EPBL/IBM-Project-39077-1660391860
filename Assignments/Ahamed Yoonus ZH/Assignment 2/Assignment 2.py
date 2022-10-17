
'''/* Problem Statement : Build a python code where you get temperature and humidity by using random function ,and continous  */
    monitor temperatur and humidity and alert the user if it is Too hot or Too Cold */
'''

import random
from time import sleep

Temp=0.0
Humid=0.0

while True:

    Temp = random.random()*100
    # Multipling by 100 because random function generate a random float value between 0 to 1
    Humid = random.random()*100

    if((Temp > 40) and (Humid < 30) ):
        print("Temperatur is very hight")
        print("Temperature : {:.2f} ".format(Temp))
        print("Humidity : {:.2f} ".format(Humid))
    
    elif((Temp < 30) and (Humid >50) ):
        print("Temperature is Low")
        print("Temperature : {:.2f} ".format(Temp))
        print("Humidity : {:.2f} ".format(Humid))

    else:
        print("reading....")
    sleep(1)
#sleep function delay the execution of the next instruction the delay time can be set by the users`


