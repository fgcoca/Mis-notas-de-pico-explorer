# --1--> Importar los módulos necesarios
import machine, neopixel
import time # <--1--

# --2--> Crear objeto definiendo el pin y el numero de LEDs
np = neopixel.NeoPixel(machine.Pin(0), 8) # <--2--

# --3--> Funcion con las distintas secuencias
def demo(np):
    n = np.n # Numero de LEDs
    
    # Ruleta de encendido en blanco a brillo maximo
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(100)

    # Efecto rebote
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(100)

    # Fundido rojo de menos a mas brillo y viceversa
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()
        time.sleep_ms(50)
   
   # Apagado
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    time.sleep(3)
# <--4--

while True:
    demo(np)