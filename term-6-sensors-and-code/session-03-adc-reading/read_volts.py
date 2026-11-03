# read_volts.py
# voltazh-e GPIO 34 ra mikhanad va be volt tabdil mikonad.
from machine import Pin, ADC
import time

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)

while True:
    raw = sensor.read()
    volts = raw * 3.3 / 4095
    print(raw, round(volts, 2))
    time.sleep(0.5)
