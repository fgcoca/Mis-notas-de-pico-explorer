from machine import Pin

led = Pin(5, Pin.OUT)

#crea 'pulsador' y habilita su resistencia pull-up
pulsador = Pin(4, Pin.IN, Pin.PULL_UP)

try:
    while True:
        if not pulsador.value():
            led.value(1)
        else:
            led.value(0)
except:
    pass
