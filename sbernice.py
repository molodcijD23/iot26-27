import dht
from machine import Pin
import tm1637
import time

# DHT22
sensor = dht.DHT22(Pin(15))

# TM1637
display = tm1637.TM1637(
    clk=Pin(14),
    dio=Pin(13)
)

while True:
    try:
        sensor.measure()

        temperature = round(sensor.temperature())
        humidity = round(sensor.humidity())

        # první 2 znaky = teplota
        # druhé 2 znaky = vlhkost
        display.show("{:02d}{:02d}".format(temperature, humidity))

        print("Teplota:", temperature, "°C")
        print("Vlhkost:", humidity, "%")

    except OSError:
        print("Chyba při čtení DHT22")

    time.sleep(2)