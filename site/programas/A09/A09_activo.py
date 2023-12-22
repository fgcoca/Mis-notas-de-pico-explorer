from machine import Pin
import time

boton = Pin(1, Pin.IN, Pin.PULL_UP)
buzzer = Pin(0, Pin.OUT)
 
while True:
    if boton.value() == 0:
        print("Boton pulsado")
        buzzer.value(1)
        time.sleep(1)
    else:
        buzzer.value(0)