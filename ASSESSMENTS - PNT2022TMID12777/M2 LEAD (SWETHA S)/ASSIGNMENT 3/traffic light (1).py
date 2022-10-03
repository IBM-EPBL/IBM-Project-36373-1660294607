from gpiozero import LED
from time import sleep
#importing inbuilt functions
#5,6,13 indicates gpio pins
green= LED(5)
red= LED(6)
blue= LED(13)
while True:
#initially all the lights are off
    green.off()
    red.off()
    blue.off()
    sleep(1)
#green led will on for 1s
    green.on()
    sleep(1)
#green led will turn off after 1s and red led will turn on
    green.off()
    red.on()
    sleep (1)
    red.off()
    blue.on()
    sleep(1)
  
  

