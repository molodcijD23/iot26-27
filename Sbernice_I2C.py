from machine import Pin, I2C
import time

# I2C
i2c = I2C(
    1,
    scl=Pin(3),
    sda=Pin(2),
    freq=100000
)

LCD_ADDR = 0x27

# Podsvícení
BACKLIGHT = 0x08

# Řídicí bity
EN = 0x04
RS = 0x01


def send_byte(data):
    i2c.writeto(LCD_ADDR, bytes([data | BACKLIGHT]))


def pulse_enable(data):
    send_byte(data | EN)
    time.sleep_us(500)
    send_byte(data & ~EN)
    time.sleep_us(500)


def send_command(cmd):
    high = cmd & 0xF0
    low = (cmd << 4) & 0xF0

    pulse_enable(high)
    pulse_enable(low)


def send_data(data):
    high = (data & 0xF0) | RS
    low = ((data << 4) & 0xF0) | RS

    pulse_enable(high)
    pulse_enable(low)


def lcd_init():
    time.sleep_ms(50)

    send_command(0x33)
    send_command(0x32)
    send_command(0x28)
    send_command(0x0C)
    send_command(0x06)
    send_command(0x01)

    time.sleep_ms(5)


def lcd_print(text):
    for char in text:
        send_data(ord(char))


def lcd_set_cursor(row, column):
    if row == 0:
        address = 0x80 + column
    else:
        address = 0xC0 + column

    send_command(address)


# Inicializace
lcd_init()

# První řádek
lcd_set_cursor(0, 0)
lcd_print("Hello Pico W!")

# Druhý řádek
lcd_set_cursor(1, 0)
lcd_print("I2C funguje!")