# guard_design.py
# negahban-e tariki: ADC rooye GPIO 34, transistor rooye GPIO 25, buzzer rooye GPIO 4.
from machine import Pin, ADC, PWM
import time

THRESHOLD = 0.55

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)
lamp = Pin(25, Pin.OUT)
buzzer = PWM(Pin(4), freq=880)
buzzer.duty(0)

while True:
    volts = sensor.read() * 3.3 / 4095
    print(round(volts, 2))
    if volts < THRESHOLD:
        lamp.on()
        buzzer.duty(512)
    else:
        lamp.off()
        buzzer.duty(0)
    time.sleep(0.5)
