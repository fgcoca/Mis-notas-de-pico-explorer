# --1--> Importar los módulos necesarios
from machine import Pin, PWM
import time # <--1--

# --2--> Configurar pines GP3, GP4 y GP5 como salidas PWM y frecuencia de 1 kHz
pines = [3,4,5]
frecuencia = 1000

pwm0 = PWM(Pin(pines[0]))
pwm1 = PWM(Pin(pines[1]))
pwm2 = PWM(Pin(pines[2]))
pwm0.freq(frecuencia)
pwm1.freq(frecuencia)
pwm2.freq(frecuencia) # <--2--

# --3--> Definicion de funcion para que variable rgb represente el valor RGB
# El rango PWM es 0 a 65535 (2^16). Se obtiene el cada canal con una operación
# a nivel de bit.
def establecer_color(rgb):
    pwm0.duty_u16(65535 - (rgb >> 4))
    pwm1.duty_u16(65535 - (rgb >> 1))
    pwm2.duty_u16(65535 - (rgb >> 0)) #<--3--

# --4--> La función rueda() es un método de selección de color del modelo de
# color introducido en establecer_color(). El rango de valores del parámetro
# parámetro posicion es 0-65535. La función devolverá un dato que contiene
# el valor del ciclo de trabajo
def rueda(posicion):
    posicion_rueda = posicion % 65535
    if posicion_rueda < 21845:
        return (((65535 - posicion_rueda*3) << 4) | ((posicion_rueda*3) << 1))
    elif posicion_rueda >= 21845 and posicion_rueda < 43690:
        posicion_rueda -= 21845
        return (((65535 - posicion_rueda*3) << 1) | (posicion_rueda*3))
    else:
        posicion_rueda -= 43690
        return (((posicion_rueda*3) << 4) | (65535 - posicion_rueda*3)) # <--4--
        
try:
    while True:
        #--5--> Recorrer el rango de valores invocando a rueda() con un valor
        # cada 5ms
        for i in range(0, 65535):
            establecer_color(rueda(i))
            time.sleep_ms(5) # <--5--
except:
    #--6--> Apagado de los temporizadores de hardware
    pwm0.deinit()
    pwm1.deinit()
    pwm2.deinit() # <--6--