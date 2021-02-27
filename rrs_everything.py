# everything.py
# https://dronebotworkshop.com

import machine
import utime

potentiometer = machine.ADC(26)

mtr_AI1 = machine.Pin(8, machine.Pin.OUT)
mtr_AI2 = machine.Pin(7, machine.Pin.OUT)
mtr_PWMa = machine.PWM(machine.Pin(6))

button_red = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_black = machine.Pin(2,machine.Pin.IN, machine.Pin.PULL_UP)

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

sda = machine.Pin(20)
scl = machine.Pin(21)

i2c = machine.I2C(0,sda=sda, scl=scl, freq=400000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

oled.text('Pico Motor Test', 0, 0)
oled.show()
utime.sleep(2)

led_red.value(1)
led_green.value(0)
led_blue.value(0)
utime.sleep(2)

led_red.value(0)
led_green.value(1)
led_blue.value(0)
utime.sleep(2)

led_red.value(0)
led_green.value(0)
led_blue.value(1)
utime.sleep(2)

mtr_PWMa.freq(50)
mtr_AI1.value(0)
mtr_AI2.value(0) # set direction of motor

while True:
    
    speedvalue = int((potentiometer.read_u16())/500)
    
    mtr_PWMa.duty_u16(potentiometer.read_u16())
    
    if button_red.value() == 1:
        mtr_AI1.value(0)
        mtr_AI2.value(1)
        led_red.value(1)
        led_green.value(0)
        led_blue.value(0)
        
    if button_black.value() == 0:
        mtr_AI1.value(1)
        mtr_AI2.value(0)
        led_red.value(0)
        led_green.value(1)
        led_blue.value(0)
        
    if button_red.value() == 0 and button_black.value() == 1:
        mtr_AI1.value(0)
        mtr_AI2.value(0)
        led_red.value(0)
        led_green.value(0)
        led_blue.value(1)
        
    oled.fill_rect(1, 15, speedvalue,25,1)
    oled.show()
    oled.fill_rect(1, 15, speedvalue,25,0)
    utime.sleep(0.25)
        
        
        
                    
    
   


