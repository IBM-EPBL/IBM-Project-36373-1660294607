import random
#randint  returns a integer number between -40 and 120(both start and end values are  included)
def Humidityvalue():
  Humidity = random.randint(0, 100)
  return Humidity
def Temperature():
  Temp = random.randint(-40, 120)
  return Temp
Humidity = Humidityvalue()
Temp = Temperature()
print("Humidity value: ", Humidity)
print("Temperature value: ",Temp)
#checking the climate condition based on temperature values
if Temp >= -40 and Temp <= 0:
  print("chill")
elif Temp >= 0 and Temp <= 100:
  print("temperature is normal")
else:
  print("high temperature make a alarm")
  
