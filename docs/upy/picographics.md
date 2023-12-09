# <FONT COLOR=#8B008B>La libreria PicoGrphics</font>
Pico Graphics es la biblioteca de visualización y gráficos para controlar pantallas desde la Pico en MicroPython.

## <FONT COLOR=#007575>**Configuración de Pico Grphics**</font>
Para utilizar las funciones de la biblioteca tenemos que crear una instancia de PicoGrphics:

~~~py
from picographics import PicoGraphics, DISPLAY_LCD_160X80

pantalla = PicoGraphics(display=DISPLAY_LCD_160X80)
~~~

La precaución a tener en cuenta es que MicroPython solamente dispone de 192 KB de RAM y una pantalla RGB de 320x240 utiliza 150 KB.

### <FONT COLOR=#AA0000>Pantallas compatibles</font>

* Pantalla Pico - LCD SPI de 240x135 -```DISPLAY_PICO_DISPLAY```
* Pantalla Pico 2 - LCD SPI de 320x240 -```DISPLAY_PICO_DISPLAY_2```
* Tufty 2040 - LCD paralelo 320x240 -```DISPLAY_TUFTY_2040```
* **Pico Explorer - LCD SPI de 240x240 -```DISPLAY_PICO_EXPLORER```**
* Enviro Plus - LCD SPI de 240x240 -```DISPLAY_ENVIRO_PLUS```
* Conexión LCD SPI redonda de 240x240 -```DISPLAY_ROUND_LCD_240X240```
* Conexión LCD SPI cuadrada de 240x240 -```DISPLAY_LCD_240X240```
* Conexión LCD SPI de 160x80 -```DISPLAY_LCD_160X80```
* OLED 128x128 I2C -```DISPLAY_I2C_OLED_128X128```
* Pico Inky Pack / Badger 2040 / Badger 2040 W - Tinta E monocromática 296x128 -```DISPLAY_INKY_PACK```
* Inky Frame 5.7" - 600x448 Tinta electrónica de 7 colores -```DISPLAY_INKY_FRAME```
* Inky Frame 4.0" - 640x400 Tinta electrónica de 7 colores -```DISPLAY_INKY_FRAME_4```
* Inky Frame 7.3" - 800x480 Tinta electrónica de 7 colores -```DISPLAY_INKY_FRAME_7```
* Paquete Pico GFX - Matriz LCD mono 128x64 -```DISPLAY_GFX_PACK```
* Unicornio Galáctico - Matriz LED 53x11 ​​-```DISPLAY_GALACTIC_UNICORN```
* Interstate75 y 75W - Controlador Matrix HUB75 - ```DISPLAY_INTERSTATE75_SIZEOFMATRIX```
* Unicornio Cósmico - Matriz LED 32x32 -```DISPLAY_COSMIC_UNICORN```
* Unicornio Estelar - Matriz LED 16x16 -```DISPLAY_STELLAR_UNICORN```
* Pack Pico Unicornio - Matriz LED 16x7 -```DISPLAY_UNICORN_PACK```

### <FONT COLOR=#AA0000>Configuraciones disponibles</font>

* Matriz 32 x 32 -```DISPLAY_INTERSTATE75_32X32```
* Matriz 64 x 32 -```DISPLAY_INTERSTATE75_64X32```
* Matriz 96 x 32 -```DISPLAY_INTERSTATE75_96X32```
* Matriz 128 x 32 -```DISPLAY_INTERSTATE75_128X32```
* Matriz 64 x 64 -```DISPLAY_INTERSTATE75_64X64```
* Matriz de 128 x 64 -```DISPLAY_INTERSTATE75_128X64```
* Matriz de 192 x 64 -```DISPLAY_INTERSTATE75_192X64```
* Matriz de 256 x 64 -```DISPLAY_INTERSTATE75_256X64```

### <FONT COLOR=#AA0000>Modos gráficos soportados (tipo de pluma)</font>

* 1 bit - ```PEN_1BIT```- mono, utilizado para Pico Inky Pack y OLED I2C
* 3 bits - ```PEN_3BIT```- 8 colores, utilizado para Inky Frame
* 4 bits - ```PEN_P4```- Paleta de 16 colores
* 8 bits - ```PEN_P8```- Paleta de 256 colores
* RGB332 de 8 bits - ```PEN_RGB332```- 256 colores fijos (3 bits de rojo, 3 bits de verde, 2 bits de azul)
* RGB565 de 16 bits - ```PEN_RGB565```- 64K colores a costa de RAM. (5 bits rojos, 6 bits verdes, 5 bits azules)
* RGB888 de 24 bits: ```PEN_RGB88816``` 16 millones de colores a costa de mucha RAM. (8 bits rojos, 8 bits verdes, 8 bits azules)

En la mayoría de los casos  es suficiente con utilizar ```RGB332``` que ofrece un buen equilibrio entre RAM y colores disponibles y además es el valor por defecto de las pantallas LCD a color. En el ejemplo vemos la manera por defecto de configuración y la manera explicita, que en este caso son idénticas.

~~~py
display = PicoGraphics(display=PICO_DISPLAY) # por defecto
display = PicoGraphics(display=PICO_DISPLAY, pen_type=PEN_RGB332) #explicita
~~~

### <FONT COLOR=#AA0000>Rotaciones</font>
Las pantallas LED SPI admiten rotaciones de 0, 90, 180 y 270 grados y se realizan comovemos en el ejemplo:

~~~py
display = PicoGraphics(display=PICO_DISPLAY, rotate=180)
~~~

### <FONT COLOR=#AA0000>Pines personalizados</font>

#### <FONT COLOR=#880088>SPI/paralelo</font>
La biblioteca ```pimoroni_bus``` incluye ```SPIBus``` LCD SPI y ```ParallelBus``` LCD paralelo. Normalmente solamente tendremos que recurrir a usarlos si conectamos varias pantallas LCD. En el ejemplo vemos un bus SPI personalizado:

~~~py
from pimoroni_bus import SPIBus
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_RGB332

busspi = SPIBus(cs=17, dc=16, sck=18, mosi=19)

pantalla = PicoGraphics(display=DISPLAY_PICO_EXPLORER, bus=busspi, pen_type=PEN_RGB332)
~~~

#### <FONT COLOR=#880088>I2C</font>
La biblioteca ```pimoroni_i2c``` incluye ```PimoroniI2C``` lo que se puede utilizar para cambiar los pines utilizados por una OLED mono:

~~~py
from pimoroni_i2c import PimoroniI2C
from picographics import PicoGraphics, DISPLAY_I2C_OLED_128X128

busi2c = PimoroniI2C(4, 5)

pantalla = PicoGraphics(display=DISPLAY_I2C_OLED_128X128, bus=busi2c)
~~~

## <FONT COLOR=#007575>**Funciones**</font>

### <FONT COLOR=#AA0000>Generales</font>

#### <FONT COLOR=#880088>Crear y configurar plumas</font>
Para crear una pluma para los modos RGB888, RGB565, RGB332, P8 y P4 creamos una instancia de pluma así:

~~~py
mi_pluma = display.create_pen(R, G, B)
~~~

Para los modos RGB565 y RGB332 se indican los valores mediante RGB mediante números enteros que representan un color y retorna el resultado.

Para los modos P4 y P8 se consume una entrada de paleta o retorna error si la paleta está llena. Los colores se almacenan como RGB y se convierten al mostrarse en pantalla.

También es posible especificar un pluma a partir de valores HSV (Hue = Tono, Saturation = Saturación, Value = Valor) entre 0.0 y 1.0. Esto evita la necesidad de calcular el resultado RGB en Python.

~~~py
display.create_pen_hsv(H,S,V)
display.set_pen(mi_pluma) # para indicar a PicoGrphics que pluma usar
~~~

Para los modos monocromáticos las plumas se manejan de forma un poco diferente dado que especificar un color RGB no tiene sentido. En lugar de esto se pueden indicar 16 tonos de gris que van desde 0 para el negro (o gris mas oscuro) hasta el 15 (o gris mas claro) para el blanco. Simplemente tenemos que invocar ```set_pen``` indicando el tono deseado:

~~~py
display.set_pen(0)   # negro
display.set_pen(5)   # gris oscuro
display.set_pen(10)  # gris claro
display.set_pen(15)  # Blanco
~~~

Debemos tener presente que los grises funcionan mezclando pixeles blancos y negros para simularlos por lo que detalles pequeños, texto, lineas o pixeles sueltos se verán como blancos o negros.

Las pantallas Inky Frame admiten los siguientes:

* BLACK= 0
* WHITE= 1
* GREEN= 2
* BLUE= 3
* RED= 4
* YELLOW= 5
* ORANGE= 6
* TAUPE= 7 (limpieza de la pantalla)

#### <FONT COLOR=#880088>Luz de fondo</font>
Es posible configurar el brillo de la retroiluminación de la pantalla entre 0.0 y 1.0:

~~~py
display.set_backlight(0.5)
~~~

Recordemos que esto no está disponible para la  pantalla montada en la placa Pico Explorer.

#### <FONT COLOR=#880088>Límites de dibujo</font>
Se trata de establecer los límites o recorte para dibujar:

~~~py
display.set_clip(x, y, w, h) # coordenadas origen x,y y ancho y alto
~~~

Eliminar los límites de recorte:

~~~py
display.remove_clip()
~~~

#### <FONT COLOR=#880088>Limpiar</font>
Borra la pantalla al color de la pluma actual:

~~~py
display.clear()
~~~

Esto equivale a:

~~~py
w, h = display.get_bounds()
display.rectangle(0, 0, w, h)
~~~

Indicando que se pueden borrar partes de la pantalla con rectángulos para ahorrar tiempo y no tener que volver a dibujar elementos como archivos JPEG o gráficos.

#### <FONT COLOR=#880088>Actualizar</font>
Envía el contenido del buffer de Pico Grphics a la pantalla:

~~~py
display.update()
~~~

#### <FONT COLOR=#880088>Límites</font>
Podemos utilizar ```get_bounds()``` para determinar el ancho y el alto de la pantalla.

~~~py
WIDTH, HEIGHT = display.get_bounds()
~~~

### <FONT COLOR=#AA0000>Texto</font>

#### <FONT COLOR=#880088>Cambiar fuente</font>
La sintaxis genérica es:

~~~py
display.set_font(fuente)
~~~

Las fuentes disponibles están divididas en dos grupos, las de mapa de bits y las vectoriales:

**1.- Mapa de bits**. Se alinean desde su esquina superior izquierda.

>
- bitmap6
- bitmap8
- bitmap14_outline

**2.- Vectoriales**. Se alinean horizontalmente respecto a su borde izquierdo y verticalmente respecto a su línea media. Cuando ```scale=1```el borde superior de las letras mayúsculas está 10 pixeles mas arriba del ```y``` especificado y la línea base 10 pixeles por debajo.

>
- sans
- gothic
- cursive
- serif_italic
- serif

#### <FONT COLOR=#880088>Espesor</font>
De manera predeterminada las fuentes vectoriales tienen un grosor de un pixel, lo que genera texto muy fino y a veces ilegible. En la libreria tenemos el método ```set_thickness``` que permite cambiar el grosor de las líneas que configuran cada caracter de la fuente.

~~~py
display.set_thickness(n)
~~~

Dibujar textos muy gruesos ralentiza mucho el dibujo de los caracteres.

#### <FONT COLOR=#880088>Dibujando texto</font>
Para escribir un texto hacemos:

~~~py
display.text(text, x, y, wordwrap, scale, angle, spacing)
~~~

Donde:

* ```text```- cadena de texto para dibujar
* ```x```- coordenada X
* ```y```- coordenada Y
* ```wordwrap```- número de píxeles de ancho antes de intentar dividir el texto en varias líneas
* ```scale```- tamaño
* ```angle```- ángulo de rotación (solo para vectoriales)
* ```spacing```- espaciado entre letras
* ```fixed_width```- espaciar todos los caracteres a la misma distancia (monoespaciado)

La escala del texto puede ser un número entero (int) para fuentes de mapa de bits o un decimal (float) para fuentes vectoriales.

El ejemplo:

~~~py
display.set_font("bitmap8")
display.text("Hello World", 0, 0, scale=2)
~~~

Dibuja "Hello World" con la fuente bitmap8 de 16 píxeles de alto y escala 2x.

A veces es posible que necesitemos medir la longitud de una cadena de texto para centrarla o alinearla en la pantalla; se puede hacer con:

~~~py
width = display.measure_text(text, scale, spacing, fixed_width)
~~~

La altura de cada fuente Bitmap está explícita en su nombre.

Para escribir un solo carácter:

~~~py
display.character(char, x, y, scale)
~~~

Se utiliza un ```char``` del [código ASCII](https://es.wikipedia.org/wiki/ASCII) decimal. Tenemos que tener en cuenta que no todos los caracteres son compatibles.

Por ejemplo:

~~~py
display.set_font("bitmap8")
display.character(38, 0, 0, scale=2)
~~~

Dibuja un signo ampersand (&) en una versión escalada 2x de 16 píxeles de alto de la fuente 'bitmap8'.

### <FONT COLOR=#AA0000>Formas básicas</font>

#### <FONT COLOR=#880088>Línea</font>
Para dibujar una recta entre dos puntos dados usamos:

~~~py
display.line(x1, y1, x2, y2)
~~~

Las coordenadas x1,y1 definen el punto de inicio y x2,y2 el punto final de la recta.

Si necesitamos grosor en la línea mayor que el que tiene por defecto podemos hacer:

~~~py
display.line(x1, y1, x2, y2, thickness)
~~~

#### <FONT COLOR=#880088>Círculo</font>
Para dibujar un círculo hacemos:

~~~py
display.circle(x, y, r)
~~~

Siendo el punto x,y el centro del círculo y 'r' su radio.

#### <FONT COLOR=#880088>Rectángulo</font>
Dibujamos un rectángulo haciendo:

~~~py
display.rectangle(x, y, w, h)
~~~

El rectángulo tiene un vértice en X,y a partir del cual se establecen el ancho (w) y el alto (h).

#### <FONT COLOR=#880088>Triángulo</font>
Se dibuja así:

~~~py
display.triangle(x1, y1, x2, y2, x3, y3)
~~~

Cada par de coordenadas definen un vértice del triángulo.

#### <FONT COLOR=#880088>Polígono</font>
Para dibujar otras formas, podemos proporcionar una lista de puntos a ```polygon```:

~~~py
display.polygon([
  (0, 10),
  (20, 10),
  (20, 0),
  (30, 20),
  (20, 30),
  (20, 20),
  (0, 20),
])
~~~

#### <FONT COLOR=#880088>Ejemplo de dibujo</font>

~~~py
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
~~~

El programa lo podemos descargar desde este [enlace](../programas/ejem_dibujos.py)

### <FONT COLOR=#AA0000>Pixeles</font>
Hacer tareas de dibujar o escribir pixel a pixel es lento y tedioso, pero a veces hay que utilizarlo y para ello tenemos dos opciones:

* **Pixel a pixel**: ```display.pixel(x,y)```
* **Tramo horizontal de pixeles**: display.pixel_span(x,y,longitud)

En el ejemplo siguiente se utilizan ambas sentencias.

~~~py
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
BLANCO = display.create_pen(255, 255, 255)
display.set_pen(BLANCO)
# dibujo de 4 pixeles contiguos para que se aprecien bien
display.pixel(20,30)
display.pixel(20,31)
display.pixel(21,30)
display.pixel(21,31)
display.pixel_span(20,50,80)
display.update()
~~~

### <FONT COLOR=#AA0000>Gestion de paletas</font>
Los modos P4 y P8 tienen paletas de 16 y 256 colores respectivamente. Se definen colores en la paleta a partir de una lista de tuplas RGB.

~~~py
display.set_palette([
  (r, g, b),
  (r, g, b),
  (r, g, b)
])
~~~

Es posible modificar la paleta en un color dado redifiniendo el RGB por su índice:

~~~py
display.update_pen(index, r, g, b)
~~~

Para restablecer una pluma a su valor predeterminado hacemos:

~~~py
display.reset_pen(index)
~~~

Para convertir entre formatos de color tenemos:

* ```RGB332_to_RGB```
* ```RGB_to_RGB332```
* ```RGB565_to_RGB```
* ```RGB_to_RGB565```
