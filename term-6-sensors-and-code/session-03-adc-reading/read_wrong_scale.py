# read_wrong_scale.py
# khata-ye amdi: 1023 be jaye 4095.
from machine import Pin, ADC
import time

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)

while True:
    raw = sensor.read()
    volts = raw * 3.3 / 1023
    print(raw, round(volts, 2))
    time.sleep(0.5)
