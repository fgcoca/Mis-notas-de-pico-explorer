# <FONT COLOR=#8B008B>Introducción a Python</font>

## <FONT COLOR=#007575>**¿Que es Python y de donde viene?**</font>
Una breve introducción a cosas de Python que nos pueden ayudar con la guía de MicroPython. Al final se trata el asunto de los permisos en Linux, que aunque sea un poco "off topic" puede resultar útil.

### <FONT COLOR=#AA0000>Creador de Python</font>
Python es un lenguaje de programación interpretado (no hay que compilar los programas) cuya filosofía hace hincapié en una sintaxis que favorezca un código legible.

Python fue creado a finales de los ochenta, por el holandés [Guido van Rossum](https://es.wikipedia.org/wiki/Guido_van_Rossum) en el Centro para las Matemáticas y la Informática (CWI, Centrum Wiskunde & Informatica), en los Países Bajos.

El nombre del lenguaje proviene de la afición de su creador por los humoristas británicos Monty Python y no de la serpiente del mismo nombre. Aunque se suele usar un símbolo con una serpiente pitón para representarlo, de ahí la normal confusión.

Se trata de un lenguaje de programación multiparadigma o que soporta más de un paradigma de programación, representando un paradigma un enfoque particular o filosofía para la construcción del software. Python soporta:

* Orientación a objetos. En la programación orientada a objetos (OOP) los objetos manipulan los datos de entrada para la obtención de datos de salida específicos, donde cada objeto ofrece una funcionalidad especial. Los objetos permiten la agrupación en librerías y usualmente permiten al usuario la creación de sus propias librerías. Se basa en técnicas de herencia, cohesión, abstracción, polimorfismo, acoplamiento y encapsulamiento.
* Programación imperativa. Es la forma natural de programar un ordenador, es el estilo de programación que se utiliza en el ensamblador y el más cercano a la máquina. Sigue la arquitectura arquitectura clásica de Von Newmann con una memoria donde se almacenan los datos y el programa y una unidad de control que ejecuta las instrucciones del programa, conocida cómo contador del programa.
* Programación funcional. Es un estilo de programación cuyo método básico de computación es la aplicación de funciones a sus argumentos.

### <FONT COLOR=#AA0000>Filosofía Python</font>
Es muy parecida a la filosofía de Unix. El código que sigue los principios de Python de legibilidad y transparencia se dice que es "**pythonic**". Por el contrario, el código opaco u ofuscado es bautizado como "**unpythonic**". Los puntos que describen su filosofia son:

* Bello es mejor que feo.
* Explícito es mejor que implícito.
* Simple es mejor que complejo.
* Complejo es mejor que complicado.
* Plano es mejor que anidado.
* Disperso es mejor que denso.
* La legibilidad cuenta.
* Los casos especiales no son tan especiales como para quebrantar las reglas.
* Lo práctico gana a lo puro.
* Los errores nunca deberían dejarse pasar silenciosamente.
* A menos que hayan sido silenciados explícitamente.
* Frente a la ambigüedad, rechaza la tentación de adivinar.
* Debería haber una -y preferiblemente sólo una- manera obvia de hacerlo.
* Aunque esa manera puede no ser obvia al principio a menos que usted sea holandés (en clara referencia a su autor).
* Ahora es mejor que nunca.
* Aunque nunca es a menudo mejor que ya mismo.
* Si la implementación es difícil de explicar, es una mala idea.
* Si la implementación es fácil de explicar, puede que sea una buena idea.
* Los espacios de nombres (namespaces) son una gran idea **¡Hagamos más de esas cosas!**

El Zen de Python viene incorporado (en inglés) a partir de la versión 2.1.2 y podemos invocarlo con ```import this``` abriendo Python en una terminal en un sistema en el que lo tengamos instalado, lógicamente.

<center>

![Arrastrar y soltar un fragmento de código](../img/guias/intro/zen.png)  
*Arrastrar y soltar un fragmento de código*

</center>
