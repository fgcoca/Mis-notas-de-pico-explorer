from machine import Pin
import time

pines = [0, 1, 2, 3, 4, 5, 6, 7, 27, 28] #27 y 28 son ADC0 y ADC1
def mostrarBarras(): 
    time.sleep(1) # parada entre recorridos
    for pin in pines:
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(300)
        led.value(0)
        time.sleep_ms(300)        
    time.sleep(1) # parada entre recorridos
    for pin in reversed(pines):
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(300)
        led.value(0)
        time.sleep_ms(300)
          
while True:
    mostrarBarras()
    
