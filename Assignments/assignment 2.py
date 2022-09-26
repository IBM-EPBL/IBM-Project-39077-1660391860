import random
from time import sleep


Temp = 0.0
Humid =0.0

while True:

    Temp = random.random()*100
    Humid = random.random()*100
    if((Temp>50) and(Humid<30)):
        print("Temperature is very high")
        print("Temperature : {:.2f} ".format(Temp))
        print("Humidity : {:.2f} ".format(Humid))
    
    elif((Temp < 20) and (Humid >50) ):
        print("Temperature is very Low")
        print("Temperature : {:.2f} ".format(Temp))
        print("Humidity : {:.2f} ".format(Humid))

    else:
        print("reading....")
    sleep(2)



