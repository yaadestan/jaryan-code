# guard_low_threshold.py
# khata-ye amdi: astane zir-e har do adad.
from machine import Pin, ADC, PWM, I2C
import ssd1306
import time

THRESHOLD = 0.2

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)
lamp = Pin(25, Pin.OUT)
buzzer = PWM(Pin(4), freq=880)
buzzer.duty(0)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    volts = sensor.read() * 3.3 / 4095
    print(round(volts, 2))
    oled.fill(0)
    oled.text(str(round(volts, 2)) + " V", 0, 0)
    if volts < THRESHOLD:
        lamp.on()
        buzzer.duty(512)
        oled.text("DARK", 0, 20)
    else:
        lamp.off()
        buzzer.duty(0)
        oled.text("LIGHT", 0, 20)
    oled.show()
    time.sleep(0.5)
