# read_light.py
# LDR rooye GPIO 35: hamin barname, paye-ye digar.
from machine import Pin, ADC
import time

sensor = ADC(Pin(35))
sensor.atten(ADC.ATTN_11DB)

while True:
    raw = sensor.read()
    volts = raw * 3.3 / 4095
    print(raw, round(volts, 2))
    time.sleep(0.5)
