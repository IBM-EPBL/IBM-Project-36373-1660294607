# Blinking of an LED using RaspberryPi
# Importing in-built functions
from gpiozero import Button, LED, Buzzer
led = LED(25)
button = Button(21)
buzzer = Buzzer(15)
while True:
    button.wait_for_press()
    led.blink(1,1)
    buzzer.on()
    button,waut_for_release()
    led.off()
    buzzer.off()
