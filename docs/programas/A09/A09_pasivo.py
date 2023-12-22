# --1--> Importar pines, PWM, time y matematicas
from machine import Pin, PWM
import math
import time # <--1--

# --2--> Contantes, variables e inicializaciones
PI = 3.14
boton = Pin(1, Pin.IN, Pin.PULL_UP)
buzzerPasivo = PWM(Pin(0))
buzzerPasivo.freq(1000) # <--2--

# --3--> Definicion de funcion
def alarma():
    for x in range(0, 36):
        # mediante la función seno se crea la frecuencia del buzzer
        Valor_seno = math.sin(x * 10 * PI / 180)
        tono = 1500 + int(Valor_seno*500)
        buzzerPasivo.freq(tono)
        time.sleep_ms(10) # <--3--

try:
    while True:
        if not boton.value():
            buzzerPasivo.duty_u16(4092*2)
            alarma()
        else:
            buzzerPasivo.duty_u16(0)
except:
    buzzerPasivo.deinit() # Cuando se deja de usar PWM se apagan temporizadores