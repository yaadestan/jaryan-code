# tone.py
# slider farkans ra be hertz midahad; buzzer rooye GPIO 4.
from machine import Pin, ADC, PWM
import time

knob = ADC(Pin(34))
knob.atten(ADC.ATTN_11DB)
buzzer = PWM(Pin(4))

hertz = round(knob.read() * 2000 / 4095)
buzzer.freq(hertz)
buzzer.duty(512)
print(hertz)

while True:
    time.sleep(0.2)
