import RPi.GPIO as GPIO
import Button, LED, Buzzer
led = LED(11)
button = Button(21)
buzzer = Buzzer(25)
while True:
    button.wait_for_press()
    led.blink(1,1)
    buzzer.on()
    button,waut_for_release()
    led.off()
    buzzer.off()
