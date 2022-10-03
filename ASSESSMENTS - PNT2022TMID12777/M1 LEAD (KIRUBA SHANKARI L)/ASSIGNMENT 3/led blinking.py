# Using in-built functions
from gpiozero import Button, LED, Buzzer
#connecting led button & buzzer to gpio pins
led = LED(18)
button = Button(16)
buzzer = Buzzer(7)
#blinking led based on button press
while True:
 button.wait_for_press()
 led.blink(1,1)
 buzzer.on()
 button.wait_for_release()
 led.off()
 buzzer.off()
