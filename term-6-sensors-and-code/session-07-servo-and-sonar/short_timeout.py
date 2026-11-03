# short_timeout.py
# khata-ye amdi: entezar faghat 1000 mikrosanie.
from machine import Pin, time_pulse_us
import time

trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

while True:
    trig.on()
    time.sleep_us(10)
    trig.off()
    us = time_pulse_us(echo, 1, 1000)
    print(us)
    time.sleep(0.5)
