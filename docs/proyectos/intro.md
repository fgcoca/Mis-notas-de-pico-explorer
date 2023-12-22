# <FONT COLOR=#8B008B>Computación física con Raspberry Pi Pico</font>
La Raspberry Pi Pico, con su microcontrolador RP2040, se ha diseñado pensando en la computación física. Dispone de numerosos pines de entrada/salida de propósito general (GPIO) que le permiten comunicarse con multitud de componentes, lo que te permite crear proyectos, que van desde encender LEDs hasta registrar datos sobre el mundo que nos rodea.

La computación física no es más difícil de aprender que la programación tradicional. Los proyectos que aquí veremos nos ayudarán a construir nuestros propios circuitos y programarlos para que que hagan lo que queramos.

En la actividad A01 hicimos nuestro primer ejemplo de computación física haciendo que se encienda y apague el LED que incorpora la placa, siendo este el ejemplo equivalente al "Hola mundo" de la programación tradicional. En el caso de la Pi Pico el "hola mundo de computación física" se puede hacer sin ningún compnente externo gracias al LED que incorpora la placa.

El resto de actividades son también computación física, pero he querido dejarlas aparte para centrar mejor el tema de proyectos completos que realicen tareas concretas.

Tanto en MicroPython como en Python es posible importar solamente una parte de una biblioteca, en lugar de toda la biblioteca. Hacerlo así puede hacer que nuestro programa utilice menos memoria, lo cual puede ser relevante según compliquemos los proyectos. Auqnue normalmente importaremos la librería completa y no una parte, vamos a describir con un sencillo ejemplo las diferencias:

~~~py
import machine # importa la libreria completa
from machine import Pin # importa solamente la función Pin de la libreria
~~~
