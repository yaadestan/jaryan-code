# siren.py
# do seda poshte sar-e ham.
from machine import Pin, PWM
import time

buzzer = PWM(Pin(4))
buzzer.duty(512)

while True:
    buzzer.freq(600)
    time.sleep(0.3)
    buzzer.freq(900)
    time.sleep(0.3)
