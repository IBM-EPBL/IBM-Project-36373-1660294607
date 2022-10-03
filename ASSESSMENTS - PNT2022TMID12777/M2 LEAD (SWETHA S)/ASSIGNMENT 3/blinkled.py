from machine import pin
from time import sleep
#importing inbuilt funxtions
value=int(input("enter second"))
#how many secs the led need to turn on and turn off
#eg sec=2,led will blink and turn off for 2sec
Led=pin(25,pin.OUT)

while True:
    Led.high()
    sleep(value)
    Led.low()
    sleep(value)
