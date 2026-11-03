# i2c_check.py
# neshani-e dastgah-ha rooye I2C ra chap mikonad; 0x3C yani 60.
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
print(i2c.scan())
