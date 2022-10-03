import RPi.GPIO as GPIO
from time import sleep
signal = TrafficLights(18,8,11)
button = Button(13)
while True:
    button.wait_for_press()
    signal.red.on()
    sleep(2)
    signal.amber.on()
    sleep(2)
    signal.green.on()
    sleep(2)
    signal.off()
