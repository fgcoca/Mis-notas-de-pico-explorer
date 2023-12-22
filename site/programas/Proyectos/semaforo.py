# --1--> Importar módulos necesarios
import machine
import utime
import _thread # <--1--

# --2--> Configurar pines y asignar a variables
led_rojo = machine.Pin(3, machine.Pin.OUT)
led_ambar = machine.Pin(4, machine.Pin.OUT)
led_verde = machine.Pin(5, machine.Pin.OUT) 
boton = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(1, machine.Pin.OUT)
global boton_pulsado # Delaracion de variable global
boton_pulsado = False # Inicializacion de variable global
# <--2--

# --3--> Funcion que actua como hilo
def leer_boton_thread():
    global boton_pulsado
    while True:
        if boton.value() == 1:
            boton_pulsado = True
        utime.sleep(0.01) #<--3--
        
_thread.start_new_thread(leer_boton_thread, ()) 

while True:
    if boton_pulsado == True:
        led_rojo.value(1)
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        global boton_pulsado
        boton_pulsado = False
    # --4--> Secuencia de encendido y apagado de los LEDs
    led_rojo.value(1)  # Enciende rojo
    utime.sleep(5)     # durante 5 segundos
    led_ambar.value(1) # Sin apagar rojo enciende ambas
    utime.sleep(2)     # durante 2 segundos
    led_rojo.value(0)  # apaga rojo
    led_ambar.value(0) # apaga ambar
    led_verde.value(1) # enciende verde
    utime.sleep(5)     # durante 5 segundos
    led_verde.value(0) # apaga verde
    led_ambar.value(1) # enciende ambar
    utime.sleep(2)     # durante 2 segundos
    led_ambar.value(0) # apaga ambar
    # <--4--

