# first_power.py
# barname-ye aval rooye bord-e vaghei: LED rooye GPIO 25 cheshmak mizanad.
from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.on()
    print("on")
    time.sleep(1)
    led.off()
    print("off")
    time.sleep(1)
