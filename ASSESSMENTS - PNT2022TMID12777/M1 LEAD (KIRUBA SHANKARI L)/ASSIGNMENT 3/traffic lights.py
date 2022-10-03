

# Creating Traffic light using RaspberryPi
from gpiozero import TrafficLights, Button
from time import sleep
signal = TrafficLights(22,8,7)
button = Button(16)
while True:
 button.wait_for_press()
 signal.red.on()
 sleep(1)
 signal.amber.on()
 sleep(1)
 signal.green.on()
 sleep(1)
 signal.off()