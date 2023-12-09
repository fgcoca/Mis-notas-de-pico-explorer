# <FONT COLOR=#8B008B>El módulo random</font>
El módulo implementa generadores de números pseudoaleatorios y este es su código fuente: [łib/random.py](https://github.com/python/cpython/blob/3.10/Lib/random.py).

Antes de cada uso del módulo random, hay que añadir la declaración ```import random``` al principio del archivo Python.

Tenemos disponibles las siguientes opciones:

* **```randint(inicio, fin)```**: Genera aleatoriamente un número entero entre los valores inicial y final.

>
  - **inicio**: Valor inicial en el rango especificado, que se incluiría en el rango.
  - **fin**: Valor final en el rango especificado, que se incluiría en el rango.
  - **random()**: Genera aleatoriamente un número de coma flotante entre 0 y 1.

* **```random.uniform(inicio, fin)```**: Genera aleatoriamente un número de coma flotante entre los valores inicial y final.

>
  - **inicio**: Valor inicial en el rango especificado, que se incluiría en el rango.
  - **fin**: Valor final en el rango especificado, que se incluiría en el rango.

* **```random.getrandbits(size)```**: Genera un aleatorio entero del tamaño especificado por ```size```.

Por ejemplo:

si size = 4, se genera un entero en el rango de 0 a 0b1111, o sea entre 0 y 15.
    
si size = 8, se genera un entero en el rango de 0 a 0b11111111, o sea entre 0 y 255.

* **```random.randrange(inicio, fin, paso)```**: Genera aleatoriamente un entero positivo en el rango de inicio a fin que se incrementa según el valor de paso.

>
  - **inicio**: Valor inicial en el rango especificado, que se incluiría en el rango.
  - **fin**: Valor final en el rango especificado, que se incluiría en el rango.
  - **paso**: Un número entero que especifica el incremento.

* **```random.seed(sed)```**: Especifica una semilla aleatoria, que suele aplicarse junto con otros generadores de números aleatorios.

>
  - **sed**: Semilla aleatoria, un punto de partida en la generación de números aleatorios.

* **```random.choice(obj)```**: Genera aleatoriamente un elemento a partir del dato ```obj```.