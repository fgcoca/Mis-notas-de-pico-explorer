from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

# Configura pantalla
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
# Crea colores de pluma para escribir con ella
BLANCO = display.create_pen(255, 255, 255)
ROJO = display.create_pen(255,0,0)
# Establece fuente y cambia el pluma a blanco
display.set_font("bitmap8")
display.set_pen(BLANCO)
# Muestra un texto
display.text("Hola Mundo desde:", 0, 0, scale=3)
# cambia pluma a rojo
display.set_pen(ROJO)
# Muestra un texto
display.text("Pico Explorer", 0, 40, scale=4)

# Actualiza la pantalla
display.update()