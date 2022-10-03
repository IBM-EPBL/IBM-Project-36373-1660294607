
#importing the random to generate random temperature and humidity values
import random

def temperature():
#setting temperature range btn 10 and 40
    temp = random.randrange(10,40)
    return temp
T = temperature()
print("Temperature measured",T)

def humidity():
#setting humidity range btn 25 and 60
    hmdty = random.randrange(25,60)
    return hmdty
H = humidity()
print("Humidity measured",H)

#condition to continuously detect alarm 
if T>30:
    print("Hot")
elif T>=20 and T<=30:
    print("Warm")
elif T<20:
    print("Cold")