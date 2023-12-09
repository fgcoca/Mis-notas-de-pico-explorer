# <FONT COLOR=#8B008B>Referencias a clases</font>

## <FONT COLOR=#007575>**Clase ```machine```**</font>
Antes de usar el módulo ```machine``` tenemos que añadir la sentencia ```import machine``` al principio del archivo Python. Algunas de las opciones del módulo son:

* **machine.freq(freq_val)**. Cuando 'freq_val' no se especifica devuelve la frecuencia de la CPU actual y si se especifica establece la frecuencia de la CPU.
* **freq_val**. Se da en Hz: 125000000Hz (125MHz).
* **machine.reset()**. Cuando se invoca a la función el programa realiza un reset.
* **machine.unique_id()**. Obtiene la dirección MAC del dispositivo.
* **machine.idle()**. Apaga cualquier función que no se esté utilizando para reducir el consumo de energia durante periodos cortos o largos. Los periféricos siguen funcionando y la ejecución se reanuda cuando se activa cualquier interrupción.
* **machine.disable_irq()**. Desactiva las peticiones de interrupción. Devuelve el estado IRQ anterior, que debe considerarse un valor opaco. Este valor de retorno debe pasarse a la función **enable_irq()** para restaurar las interrupciones a su estado original, antes de llamar a **disable_irq()**.
* **machine.enable_irq(state)**. Rehabilita las peticiones de interrupción. El parámetro **state** debe ser el valor devuelto por la última llamada a la función **disable_irq()**.
* **machine.time_pulse_us(pin, pulse_level, timeout_us=1000000, /)**. Cronometra un pulso externo en el pin indicado y devuelve la duración del pulso en microsegundos. El argumento **pulse_level** debe ser 0 para medir el tiempo de un pulso bajo y 1 para medir el tiempo de un pulso alto.

Si el valor de entrada actual del pin es diferente a **pulse_level**, la función primero (1) espera hasta que la entrada del pin sea igual a **pulse_level**, después (2) multiplica por la duración en que el pin es igual a **pulse_level**. Si el pin ya es igual a **pulse_level**, la temporización comienza directamente.

La función devolverá -2 si hubo tiempo de espera para la condición marcada con (1) arriba, y -1 si hubo tiempo de espera durante la medición principal, marcada (2) arriba. El tiempo de espera es el mismo para ambos casos y viene dado por **timeout_us** (que está en microsegundos).

## <FONT COLOR=#007575>**Clase ```time```**</font>
Este módulo implementa un subconjunto del módulo CPython correspondiente.

El módulo **time** proporciona funciones para obtener la hora y fecha actuales, medir intervalos de tiempo, y para generar retardos.

Unix utiliza la fecha estándar de 1970-01-01 00:00:00 UTC para los sistemas POSIX. Sin embargo, algunos puertos embebidos usan el año 2000-01-01 00:00:00 UTC.

Mantener la fecha/hora real del calendario requiere un Reloj en Tiempo Real (RTC). En sistemas con sistema operativo (SO) subyacente (incluyendo algunos RTOS), un RTC puede estar implícito. Establecer y mantener la hora real del calendario es responsabilidad del SO/RTOS y se realiza fuera de MicroPython, sólo utiliza la API del SO para consultar la fecha/hora. La hora actual del calendario puede establecerse usando la función **machine.RTC().datetime(tuple)**, y mantenerse por los siguientes medios:

* Mediante una batería de reserva.
* Mediante protocolo horario en red (requiere configuración por parte de un puerto/usuario).
* Configurado manualmente por un usuario cada vez que se enciende.

Si la hora real del calendario no se mantiene con un sistema/MicroPython RTC, las funciones que vamos a ver a continuación requieren referencia a la hora absoluta actual y pueden no comportarse como se espera.

Antes de utilizar el módulo ```time``` tenemos que añadir la sentencia ```import time``` al principio del archivo Python. Algunas de las opciones del módulo son:

* **time.sleep(seconds)**. Detener el número de segundos especificado por **seconds**, que puede ser un ```int``` o un ```float```. Hay placas que no aceptan este argumento como ```float``` por lo que se implementan las opciones de milisegundos y microsegundos.
* **time.sleep_ms(ms)**. Detener durante los milisegundos indicados. La función intenta proporcionar el retardo de los milisegundos indicados de manera precisa, pero puede tardar mas si el sistema tiene que atender un tarea de mayor prioridad.
* **time.sleep_us(us)**. Detener durante los microsegundos indicados. La función intenta proporcionar el retardo de los microsegundos indicados de manera precisa, pero puede tardar mas si el sistema tiene que atender un tarea de mayor prioridad.
* **time.time()**. Obtiene la marca de tiempo de la CPU en segundos.
* **time.ticks_ms()**. Devuelve el incremento del contador en milisegundos.
* **time.ticks_us()**. Devuelve el incremento del contador en microsegundos.
* **time.ticks_cpu()**. Similar a las dos anteriores pero mas exacto porque retorna el reloj de la CPU.
* **time.ticks_add(ticks, delta)**. Obtiene la marca de tiempo después del desfase, donde **ticks** puede indicarse con **ticks_ms()**,**ticks_us()** o **ticks_cpu()** y **delta** puede ser cualquier entero o expresión numérica.
* **time.ticks_diff(old_t, new_t)**. Calcula la diferencia de tiempo entre las dos marcas temporales que pueden indicarse con **ticks_ms()**,**ticks_us()** o **ticks_cpu()**. El tiempo de inicio se indica con **old_t** y el de finalización con **new_t**.

## <FONT COLOR=#007575>**Clase ```Pin(id, mode, pull, value)```**</font>
Un objeto pin se utiliza para controlar los pines de E/S (también conocidos como GPIO - entrada/salida de propósito general). Los objetos pin están comúnmente asociados con un pin físico que puede establecer un nivel de tensión de salida y leer tensiones de entrada. La clase pin tiene métodos para establecer el modo del pin (IN, OUT, etc) y métodos para obtener y establecer el nivel lógico digital. Para el control analógico de un pin, se utiliza la clase ADC.

Un objeto pin se construye utilizando un identificador que especifica inequívocamente un determinado pin de E/S. Las formas permitidas del identificador y el pin físico al que se asigna el identificador son específicas del puerto. Las posibilidades para el identificador son un entero, una cadena o una tupla con el puerto y el número de pin.

Modelos de utilización:

~~~py
from machine import Pin

# establece como pin de salida el pin0
p0 = Pin(0, Pin.OUT)

# establece el valor del pin en bajo o en alto
p0.value(0)
p0.value(1)

# crea p2 como pin de entrada y activa la resistencia de pull up del pin
p2 = Pin(2, Pin.IN, Pin.PULL_UP)

# lee e imprime el valor del pin
print(p2.value())

# reconfigura el pin0 a modo entrada y pone la resistencia pull down
p0.init(p0.IN, p0.PULL_DOWN)

# configura la llamada a una interrupción (irq callback)
p0.irq(lambda p:print(p))
~~~

Antes de utilizar el módulo ```Pin``` tenemos que añadir la sentencia ```from machine import Pin``` al principio del archivo Python. Algunas de las opciones del módulo son:

* **id**. Un número de pin.
* **mode**. El modo del pin puede establecerse como **Pin.IN**, **Pin.OUT** o **Pin.OPEN_DRAIN** para pin de entrada, de salida o de drenador abierto respectivamente.
* **Pull**. Cuando se activan los modos pull up y pull down internos. No se indica nada ni no queremos poner resistencia pull up o pull down, o **Pin.PULL_UP** para poner el modo pull-up (salida a nivel alto por defecto), o **Pin.PULL_DOWN** para establecer modo pull-down (salida a nivel bajo por defecto).
* **Value**. Nivel lógico de estado del pin, alto o bajo (1 o 0).
* **Pin.init(mode, pull)**. Inicializa los pines.
* **Pin.value([value])**. Obtiene o establece el estado de los pines, devuelve 0 o 1 según el nivel lógico de los pines. Sin parámetro, lee el nivel de entrada. Con un parámetro dado, se establece el nivel de salida. **value** puede valer ```True/False``` o ```1/0```.
* **Pin.irq(trigger, handler)**. Configura un manejador de interrupciones para ser llamado cuando el nivel del pin cumple una condición.
* [ ] **trigger**: **Pin.IRQ_FALLING** para flanco de bajada y **Pin.IRQ_RISING** para flanco de subida.
* [ ] **Handler**: Devuelve la llamada a la función.

## <FONT COLOR=#007575>**Clase PWM(pin)**</font>
Antes de cada uso del módulo PWM, tenemos que añadir la declaración ```from machine import PWM``` al principio del archivo python. Esta clase proporciona PWM.

En el ejemplo siguiente se puede ver el funcionamiento básico del uso de la clase:

~~~py
from machine import PWM # enciende el temporizador de hardware

# crea objeto PWM en un pin y establece la frecuencia y el ciclo de trabajo
pwm = PWM(pin, freq=50, duty_u16=8192)

pwm.duty_u16(32768)     # ciclo de trabajo al 50%

# reinicializa con un periodo de 200us (f=5000) y un ciclo de trabajo de 5us
pwm.init(freq=5000, duty_ns=5000)

pwm.duty_ns(3000)       # establece la anchura del pulso a 3us

pwm.deinit() # apaga el temporizador de hardware
~~~

El constructor de la clase tiene la siguiente sintaxis:

```classmachine.PWM(dest, *, freq, duty_u16, duty_ns, invert)```

que construye y retorna un objeto PWM utilizando los siguientes parámetros:

* **dest** es quien emite el PWM, que suele ser un objeto ```machine.Pin```.
* **freq** es un número entero que establece la frecuencia en Hz del ciclo PWM.
* **duty_u16** establece el ciclo de trabajo como un ratio duty_u16/65535.
* **duty_ns** establece el ancho del pulso en nanosegundos.
* **invert** invierte la salida respectiva si su valor es True

Establecer ```freq``` puede afectar a otros objetos PWM si los objetos comparten el mismo generador PWM (esto es específico del hardware). Sólo se debe especificar un duty_u16 y duty_ns si,ultaneamente. El parámetro ```invert``` no está disponible en todos los puertos.

La clase tiene disponibles los siguientes métodos:

* **PWM.init(*, freq, duty_u16, duty_ns)**. Modifica los ajustes del objeto PWM.
* **PWM.deinit()**. Desabilita la salida PWM.
* **PWM.freq([value])**. Obtiene o ajusta la frecuencia actual de la salida PWM. Sin argumentos devuelve la frecuencia en Hz. Con un único argumento de ```value```, la frecuencia se ajusta a ese valor en Hz. El método puede generar un ValueError si la frecuencia está fuera del rango válido.
* **PWM.duty_u16([value])**. Obtiene o establece el ciclo de trabajo actual de la salida PWM, como un valor de 16 bits sin signo en el rango de 0 a 65535 inclusive. Sin argumentos devuelve el ciclo de trabajo. Con un argumento de ```value``` único, el ciclo de trabajo se establece en ese valor, medido como la relación entre value/65535.
* **PWM.duty_ns**. Obtiene o establece el ancho de pulso actual de la salida PWM, como un valor en nanosegundos. Sin argumentos devuelve el ancho de pulso en nanosegundos. Con un único argumento de value, el ancho de pulso se establece en ese valor.
