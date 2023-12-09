from machine import Pin
import time

led = Pin(5, Pin.OUT)
pulsador = Pin(4, Pin.IN, Pin.PULL_UP)

def invertirGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)
    
try:
    while True:
        if not pulsador.value():
            time.sleep_ms(20)
            if not pulsador.value():
                invertirGPIO()
                while not pulsador.value():
                    time.sleep_ms(20)
except:
    pass