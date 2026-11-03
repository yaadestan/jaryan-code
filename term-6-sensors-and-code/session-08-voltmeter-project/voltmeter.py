# voltmeter.py
# voltmeter: voltazh-e GPIO 35 zarb-dar 2, rooye OLED.
from machine import Pin, ADC, I2C
import ssd1306
import time

sensor = ADC(Pin(35))
sensor.atten(ADC.ATTN_11DB)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    raw = sensor.read()
    volts = raw * 3.3 / 4095 * 2
    width = round(volts * 128 / 3.3)
    print(round(volts, 2))
    oled.fill(0)
    oled.text("Voltmeter", 0, 0)
    oled.text(str(round(volts, 2)) + " V", 0, 20)
    oled.fill_rect(0, 40, width, 10, 1)
    oled.show()
    time.sleep(0.5)
