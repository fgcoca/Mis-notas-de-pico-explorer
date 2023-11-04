# <FONT COLOR=#8B008B>Programación Orientada a Objetos</font>
Este apartado se crea especificamente por la dificultad que tiene el tema que vamos a explicar a continuación:

>Hay ciertos elementos o dispositivos que van a requerir de una librería externa a Python y estas librerias se hacen utilizando las clases. En el editor online de MicroPython de micro:bit se pueden incluir y utilizar este tipo de liberías. Para centrar un poco el tema vamos a ver:

* Las clases en Python de una forma no muy profunda.
* La utilización del menú Project de python.microbit, necesario para poder incluir librerias
* Ejemplo de trabajo con una libreria para una LCD I2C.

## <FONT COLOR=#007575>**Las clases en Python**</font>
La Programación Orientada a Objetos (POO) es un modelo de programación que proporciona unas guías acerca de cómo trabajar con él y que está basado en el concepto de clases y objetos.

Una clase es una especie de plantilla que define, de forma genérica, como serán los objetos de un determinado tipo. Pongamos por ejemplo que una clase representa a un club, que podemos denominar "club". Esta clase puede tener atributos (propiedades) como nombre, edad, profesion. Se pueden implementar como métodos (funciones) de esas propiedades comportamientos como socio, socia o imparte_taller.

Un ejemplo sencillo de un objeto puede ser un profesor, que puede ser socio por lo que se crea un atributo de profesión y además puede impartir_taller, por lo que se define un nuevo método.

Una clase en Python es una estructura que permite definir los métodos y atributos que definen un objeto. En Python una clase es una plantilla para crear objetos que son instancias de esa clase.

En Python, una clase se define mediante la palabra clave ```class```, seguida del nombre de la clase, dos puntos (:) y el cuerpo de la clase. Este cuerpo contiene definiciones de métodos y atributos, que pueden ser públicos o privados según su acceso.

~~~py
class club:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def saludo(self)
        print("Hola, me llamo " + self.nombre + "y soy " + self.profesion)
~~~

Las principales ventajas de utilizar clases son:

* **Reutilización**. Una clase la podemos reutilizar en diferentes partes del programa y en distintos programas. Esto puede ahorrar mucho tiempo y evita repeticiones de código.
* **Modulación**. El código de un programa se divide en partes mas pequeñas lo que facilita el mantenimiento y la solución de problemas.
* **Encapsulación**. Consiste en ocultar la complejidad de un objeto para mostrar solamente una interfaz simple fácil de usar para interactuar ese objeto.
* **Polimorfismo**. Se trata de implementar el mismo conjunto de métodos con diferentes comportamientos para distintos objetos. Esto dota de mayor flexibilidad al diseño de programas.

Las principales desventajas de utilizar clases son:

* **Complejidad**. Una clase puede hacer mas dificil de entender y depurar un programa debido al incremento de complejidad.
* **Curva de aprendiza**. Aprender Programación Orientada a Objetos y clases tiene una curva de aprendizaje mas pronunciada, sobre todo cuando se empieza a programar.
* **Abuso**. A veces se abusa inncesariamente de las clases en situaciones en las que una función haría lo mismo incluso de forma mas eficiente.

Las variables que se definen dentro de las clases se denominan **atributos** y sirven para almacenar datos de un objeto de esa clase. Se utilizizan para representar propiedades de un objeto.

Los atributos pueden ser como las variables normales, enteros, reales, cadenas, listas, tuplas, diccionarios, etc. Además pueden tener distintos niveles de visibilidad que se indican mediante modificadores de acceso. En Python los modificadores son públicos por defecto, lo que significa que son accesibles desde cualquier lugar del programa.

Un atributo se define como una variable que se inicializa con el método ```__init__```. Por ejemplo:

~~~py
class club:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
~~~

En la clase ```club``` los atributos nombre, edad y profesion, se definen como se ve en el código. En este caso los tres son atributos públicos de la clase ```club```, que se inicializan con los valores que se proporcionen al crear un objeto de la clase. El acceso a los atributos de un objeto de una clase se utiliza el modificador (.) seguido del nombre del atributo, por ejemplo, para acceder al atributo ```nombre``` de un objeto ```socio``` de la clase ```club``` hariamos:

~~~py
socio1 = socio1.nombre
~~~

Los tipos de atributos son:

* **Públicos**. Ya hemos indicado que se puede acceder a ellos desde cualquier parte del programa y desde fuera de la clase y que en Python lo son por defecto, por lo que no requieren ningún modificador de acceso. Se accede a ello con (.).
* **Privados**. Solo son accesibles desde la propia clase y se definen con el prefijo (__) seguido del nombre del atributo.
* **Protegidos**. Solamente son accesibles desde la propia clase o desde sus clases heredadas. Se utiliza el prefijo "" seguido del nombre del atributo para su definición. En Python es simplemente una convención y si es posible acceder desde fuera de la clase.

En Python se utilizan los **métodos**, que son funciones que se definen dentro de una clase y que se utilizan para hacer operaciones en los objetos creados a partir de esa clase. La definición de un método se realiza de la misma forma que la de una función con la diferencia de que en un método siempre tiene como primer parámetro el objeto al que se aplicará el método, que por defecto se llama ```self```.

Para **utilizar un método de una clase lo primero que tenemos que hacer es crear un objeto a partir de la clase** y así poder llamar al método sobre ese objeto.

El objeto ```self``` se utiliza como referencia del objeto que se manipula cuando se llama al método. Al crear una instancia de una clase, necesitamos diferenciar o especificar los atributos de la instancia de los argumentos y otras variables. Y ahí es donde necesitamos la palabra clave ```self``` para especificar que estamos pasando el valor a los atributos de la instancia y no a la variable o argumento local con el mismo nombre.

Existen también otros métodos que se denominan dunder (de double underscore methods) que tienen un doble guión bajo (__) al principio y al final del nombre.

* **__init__**: Inicializar un objeto cuando se crea una instancia de una clase. Se usa para asignar valores a los atributos de una instancia de clase.
* **__str__**: Se utiliza para devolver una cadena de una instancia de una clase. Es el método que se llama cuando usamos la función ```str()``` para convertir un objeto en una cadena de caracteres.
* **__repr__()**: Método especial de Python que se utiliza para devolver una cadena legible de un objeto. Se llama cuando usamos la función repr().

Y bueno, hay mas conceptos y definiciones necesarias para trabajar creando clases, pero como este no es el objetivo, lo vamos a dejar aquí que ya es suficiente para manejarnos un poco con clases ya creadas.
