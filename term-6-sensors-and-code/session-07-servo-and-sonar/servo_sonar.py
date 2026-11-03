# servo_sonar.py
# slider zaviye-ye servo ra midahad; HC-SR04 fasele ra andaze migirad.
from machine import Pin, ADC, PWM, time_pulse_us
import time

knob = ADC(Pin(34))
knob.atten(ADC.ATTN_11DB)
servo = PWM(Pin(13), freq=50)
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

angle = round(knob.read() * 180 / 4095)
duty = round(26 + angle * 97 / 180)
servo.duty(duty)
print(angle, duty)

while True:
    trig.on()
    time.sleep_us(10)
    trig.off()
    us = time_pulse_us(echo, 1, 30000)
    if us < 0:
        print("no echo")
    else:
        print(us, round(us / 58, 1))
    time.sleep(0.5)
