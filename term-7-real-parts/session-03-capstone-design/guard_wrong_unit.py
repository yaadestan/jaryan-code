# guard_wrong_unit.py
# khata-ye amdi: astane be jaye 0.55 neveshte shode 5.5.
from machine import Pin, ADC
import time

THRESHOLD = 5.5

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)
lamp = Pin(25, Pin.OUT)

while True:
    volts = sensor.read() * 3.3 / 4095
    print(round(volts, 2))
    if volts < THRESHOLD:
        lamp.on()
    else:
        lamp.off()
    time.sleep(0.5)
