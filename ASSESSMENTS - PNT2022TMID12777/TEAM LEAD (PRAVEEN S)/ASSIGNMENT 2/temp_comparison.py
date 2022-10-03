#The code is written by considering the DHT 11 - Temperature and Humidity Sensor
#The Sensor's temperature range = -20 to 60C and humidity range = 5 to 95%
#importing the random to generate random temperature and humidity values
import random 
def humidity():
    humid = random.randint(5,95)
    return humid
def temperature():
    temp = random.randint(-20,60)
    return temp
T = temperature()
H = humidity()
print("The Temperature measured is: ",T)
print("the Humidity measured is: ",H)
if T>32:
    print("That's a lot of heat out there!!")
    print("Better Stay indoors!!!")
elif T>=20 and T<=28:
    print("Everything's fine...")
elif T<20:
    print("That's too chill out there...")

