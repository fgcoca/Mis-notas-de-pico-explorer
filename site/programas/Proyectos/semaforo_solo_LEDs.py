# --1--> Importar módulos necesarios
import machine
import utime # <--1--

# --2--> Configurar pines y asignar a variables
led_rojo = machine.Pin(3, machine.Pin.OUT)
led_ambar = machine.Pin(4, machine.Pin.OUT)
led_verde = machine.Pin(5, machine.Pin.OUT) # <--2--

while True:
    # --3--> Secuencia de encendido y apagado de los LEDs
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
    # <--3--

