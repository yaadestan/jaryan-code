# voltmeter_no_scale.py
# khata-ye amdi: zarb-dar 2 ja mande ast.
from machine import Pin, ADC
import time

sensor = ADC(Pin(35))
sensor.atten(ADC.ATTN_11DB)

while True:
    raw = sensor.read()
    volts = raw * 3.3 / 4095
    print(round(volts, 2))
    time.sleep(0.5)
