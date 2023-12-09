from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
BLANCO = display.create_pen(255, 255, 255)
display.set_pen(BLANCO)
display.line(50,5,150,60)
display.line(80,5,180,60,3)
display.circle(50,100,20)
display.rectangle(100,80,50,40)
display.triangle(230,10,180,80,240,60)
display.polygon([
  (0, 10),
  (20, 10),
  (20, 0),
  (30, 15),
  (20, 30),
  (20, 20),
  (0, 20),
])
# Actualiza la pantalla
display.update()
