from machine import Pin, PWM
from random import randint
import time

pines = [3,4,5]
frecuencia = 10000

pwm0 = PWM(Pin(pines[0]))
pwm1 = PWM(Pin(pines[1]))
pwm2 = PWM(Pin(pines[2]))
pwm0.freq(frecuencia)
pwm1.freq(frecuencia)
pwm2.freq(frecuencia)

def establecer_color(r,g,b):
    pwm0.duty_u16(65535 - r)
    pwm1.duty_u16(65535 - g)
    pwm2.duty_u16(65535 - b)
    
try:
    while True:
        rojo = randint(0, 65535)
        verde = randint(0, 65535)
        azul = randint(0, 65535)
        establecer_color(rojo,verde,azul)
        time.sleep_ms(150)
except:
    pwm0.deinit()
    pwm1.deinit()
    pwm2.deinit()