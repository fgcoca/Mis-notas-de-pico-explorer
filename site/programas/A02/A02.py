from machine import Pin
import time
print(machine.freq())

led_externo = Pin(5, Pin.OUT) # pin 5 como salida

try:
    while True:
        led_externo.value(1)    # Enciende el LED
        time.sleep(0.5) # Espera medio segundo
        led_externo.value(0)    # Apaga el LED
        time.sleep(0.5) # Espera medio segundo
except:
    pass