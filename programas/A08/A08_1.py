# --1--> Importar los módulos necesarios
import machine, neopixel
import time # <--1--

# --2--> Crear objeto definiendo el pin y el numero de LEDs
np = neopixel.NeoPixel(machine.Pin(0), 8) # <--2--

while True:
    # --3--> Bucle para gradiente de rojo
    for i in range(0, 8):
        if i == 0:
            np[0] = (2, 0, 0)
        else:
            np[i] = (i*8, 0, 0)
            np.write()
            time.sleep_ms(500) # <--3--

    time.sleep(1) # Retardo entre gradientes

    # --4--> Bucle para gradiente de verde
    for i in range(0, 8):
        if i == 0:
            np[0] = (0, 2, 0)
        else:
            np[i] = (0, i*8, 0)
            np.write()
            time.sleep_ms(500) # <--4--

    time.sleep(1) # Retardo entre gradientes

    # --5--> Bucle para gradiente de azul
    for i in range(0, 8):
        if i == 0:
            np[0] = (0, 0, 2)
        else:
            np[i] = (0, 0, i*8)
            np.write()
            time.sleep_ms(500) # <--5--

    time.sleep(1) # Retardo entre gradientes

    # --5--> Apagado
    for i in range(0, 8):
        np[i] = (0, 0, 0)
        np.write() # <--5--

