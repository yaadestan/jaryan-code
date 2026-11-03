# button_led.py
# dokme rooye GPIO 32 ba pull-up: feshorde yani 0.
from machine import Pin
import time

button = Pin(32, Pin.IN)
led = Pin(25, Pin.OUT)

while True:
    state = button.value()
    print(state)
    if state == 0:
        led.on()
    else:
        led.off()
    time.sleep(0.5)
