import random
def humidity():
    humid = random.randint(15,99) 
    return humid
    
def temperature():
    temp = random.randrange(10,40) 
    return temp
T = temperature() 
H = humidity() 

print("The Temperature measured is: ",T)

print("the Humidity measured is: ",H)

if T>35:
    print("That's a lot of heat out there!!")
    
    print("Better Stay indoors!!!")
    
elif T>=24 and T<=30: 
    print("Everything's fine")
    
elif T<20: 
    print("That's too chill out there...")
