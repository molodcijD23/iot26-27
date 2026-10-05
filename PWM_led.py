from machine import Pin, PWM
import time

led = PWM(Pin(15))
led.freq(1000)

while True:
    for brightness in range(0, 65536, 500):
        led.duty_u16(brightness)
        time.sleep(0.01)

    for brightness in range(65535, -1, -500):
        led.duty_u16(brightness)
        time.sleep(0.01)