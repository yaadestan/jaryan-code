# no_pwm.py
# khata-ye amdi: paye faghat roshan mishavad, farkansi nist.
from machine import Pin
import time

buzzer = Pin(4, Pin.OUT)
buzzer.on()

while True:
    time.sleep(0.2)
