from gpiozero import Button, LED
from time import sleep
button = Button(15)
red = LED(22)
amber = LED(8)
green = LED(7)
while True:
    button.wait_for_press()
    red.on()
    button.wait_for_release()
    red.off()
    sleep(1)
    button.wait_for_press()
    amber.on()
    button.wait_for_release()
    amber.off()
    sleep(1)
    button.wait_for_press()
    green.on()
    button.wait_for_release()
    green.off()
    sleep(1)
    