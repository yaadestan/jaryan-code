# pwm_percent.py
# slider darsad-e duty ra midahad; hamin duty rooye GPIO 14 va 25 miravad.
from machine import Pin, ADC, PWM
import time

knob = ADC(Pin(34))
knob.atten(ADC.ATTN_11DB)
load_pin = PWM(Pin(14), freq=1000)
led_pin = PWM(Pin(25), freq=1000)

percent = round(knob.read() * 100 / 4095)
duty = round(percent * 1023 / 100)
load_pin.duty(duty)
led_pin.duty(duty)
print(percent, duty)

while True:
    time.sleep(0.2)
