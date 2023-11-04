from machine import Pin
import time

# Comentar una de las lineas y descomentar la otra segun version de Pico

# led = Pin(25, Pin.OUT)   # LED en la Pi Pico
led = Pin("LED", Pin.OUT) # LED en la Pi Pico

try:
    while True:
        led.value(1)    # Enciende el LED
        time.sleep(0.5) # Espera medio segundo
        led.value(0)    # Apaga el LED
        time.sleep(0.5) # Espera medio segundo
except:
    pass