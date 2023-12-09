# <FONT COLOR=#8B008B>Guía de refencia rápida de RP2</font>
RP2 hace referencia al microcontrolador RP2040.

Es muy importante leerse, si aún no lo hemos hecho, los apartados de *"Introducción"* y *"Firmware y software"* antes de continuar con esta guia rápida de MicroPython basada en los contenidos del enlace [Quick reference for the RP2](https://docs.micropython.org/en/latest/rp2/quickref.html#).

## <FONT COLOR=#007575>**Control general**</font>
Se accede al REPL de MicroPython a través del puerto serie USB. El tabulador es útil para averiguar qué métodos tiene un objeto. El modo Pegar (ctrl-E) es útil para pegar una gran cantidad de código Python en el REPL.

### <FONT COLOR=#AA0000>El módulo ```machine```</font>
El módulo contiene funciones específicas relacionadas con el hardware de una placa concreta. La mayoría de las funciones de este módulo permiten conseguir acceso directo y sin restricciones a los bloques de hardware de un sistema (como CPU, temporizadores, buses, etc.) y controlarlos.

<div class="cuadrado">

~~~py
import machine

machine.freq()          # Obtiene la frecuencia de la CPU
machine.freq(240000000) # Establece la frecuencia de la CPU a 240 MHz
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

El módulo ```machine``` contiene funciones específicas relacionadas con el hardware de una placa. La mayoría de las funciones de este módulo permiten conseguir acceso directo y sin restricciones a los bloques de hardware de un sistema (como CPU, temporizadores, buses, etc.) y controlarlos. Usado incorrectamente, esto puede llevar a un mal funcionamiento, bloqueos o cuelgues, fallos de la placa, y en casos extremos, daños en el hardware.

Todos los detalles de las funciones están en el módulo [```machine```](https://docs.micropython.org/en/latest/library/machine.html#module-machine). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Acceso a memoria</font color></font size></b>

El módulo expone tres objetos para el acceso a la memoria.

* ```machine.mem8```. Lee o escribe 8 bits de memoria.
* ```machine.mem16```. Lee o escribe 16 bits de memoria.
* ```machine.mem32```. Lee o escribe 32 bits de memoria.

Se utiliza la notación de subíndice [...] para indexar estos objetos con la dirección teniendo en cuenta que la dirección es la dirección en bytes, independientemente del tamaño de la memoria a la que se accede.

<FONT COLOR=#BB00FF><font size="5"><b>Funciones de reset</font color></font size></b>

* ```machine.reset()```
* ```machine.soft_reset()```
* ```machine.reset_cause()```
* ```machine.bootloader([value])```

<FONT COLOR=#BB00FF><font size="5"><b>Funciones relacionadas con las interrupciones</font color></font size></b>

Las siguientes funciones permiten controlar las interrupciones. Algunos sistemas necesitan interrupciones para funcionar correctamente, por lo que desactivarlas durante largos periodos de tiempo puede comprometer la funcionalidad del núcleo, por ejemplo, los temporizadores de vigilancia pueden dispararse inesperadamente. Las interrupciones sólo deben desactivarse durante un tiempo mínimo y luego volver a activarse a su estado anterior. Por ejemplo:

<div class="cuadrado">

~~~py
import machine

# Desactivar interrupciones
state = machine.disable_irq()

# Hacer una pequeña cantidad de trabajo por tiempo crítico

# Habilitar interrupciones
machine.enable_irq(state)
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

* ```machine.disable_irq()```
* ```machine.enable_irq(state)```

<FONT COLOR=#BB00FF><font size="5"><b>Funciones relacionadas con la alimentación</font color></font size></b>

* ```machine.freq([hz])```
* ```machine.idle()```
* ```machine.lightsleep([time_ms])``` - ```machine.deepsleep([time_ms])```.
* ```machine.wake_reason()```

<FONT COLOR=#BB00FF><font size="5"><b>Funciones varias</font color></font size></b>

* ```machine.unique_id()```
* ```machine.time_pulse_us(pin, pulse_level, timeout_us=1000000, /)```
* ```machine.bitstream(pin, encoding, timing, data, /)```
* ```machine.rng()```

<FONT COLOR=#BB00FF><font size="5"><b>Constantes</font color></font size></b>

* **Interrupciones:** ```machine.IDLE```, ```machine.SLEEP```, ```machine.DEEPSLEEP```
* **Causas de reinicio (reset):** ```machine.PWRON_RESET```, ```machine.HARD_RESET```, ```machine.WDT_RESET```, ```machine.DEEPSLEEP_RESET```, ```machine.SOFT_RESET```
* **Causas para despertar:** ```machine.WLAN_WAKE```, ```machine.PIN_WAKE```, ```machine.RTC_WAKE```

<FONT COLOR=#BB00FF><font size="5"><b>Clases</font color></font size></b>

* [ ] - class Pin
* [ ] - class Signal
* [ ] - class ADC
* [ ] - class ADCBlock
* [ ] - class PWM
* [ ] - class UART
* [ ] - class SPI
* [ ] - class I2C
* [ ] - class I2S
* [ ] - class RTC
* [ ] - class Timer
* [ ] - class WDT
* [ ] - class SD
* [ ] - class SDCard

### <FONT COLOR=#AA0000>El módulo ```rp2```</font>
El módulo ```rp2``` contiene funciones y clases específicas para el RP2040, tal y como se utiliza en la Raspberry Pi Pico.

<div class="cuadrado">

~~~py
import rp2
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [rp2](https://docs.micropython.org/en/latest/library/rp2.html#module-rp2). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Funciones relacionadas con PIO</font color></font size></b>

* ```rp2.asm_pio(*, out_init=None, set_init=None, sideset_init=None, in_shiftdir=0, out_shiftdir=0, autopush=False, autopull=False, push_thresh=32, pull_thresh=32, fifo_join=PIO.JOIN_NONE)```
* ```rp2.asm_pio_encode(instr, sideset_count, sideset_opt=False)```
* ```rp2.bootsel_button()```
* ```classrp2.PIOASMError```

<FONT COLOR=#BB00FF><font size="5"><b>Instrucciones en lenguaje ensamblador PIO</font color></font size></b>

Las máquinas de estado PIO se programan en un lenguaje ensamblador personalizado con nueve instrucciones máquina básicas. En MicroPython, las rutinas de ensamblado PIO se escriben como una función de Python precedida del caracter ```@rp2.asm_pio()```, y utilizan la sintaxis de Python. Dichas rutinas soportan variables y aritmética estándar de Python, así como las siguientes funciones personalizadas que codifican instrucciones PIO.

* ```wrap_target()```
* ```wrap()```
* ```label(label)```
* ```word(instr, label=None)```
* ```jmp(label)```, ```jmp(cond, label)```
* ```wait(polarity, src, index)```
* ```in_(src, bit_count)```
* ```out(dest, bit_count)```
* ```push()```, ```push(block)```, ```push(noblock)```, ```push(iffull)```, ```push(iffull, block)```, ```push(iffull, noblock)```
* ```pull()```, ```pull(block)```, ```pull(noblock)```, ```pull(ifempty)```, ```pull(ifempty, block)```, ```pull(ifempty, noblock)```
* ```mov(dest, src)```
* ```irq(index)```, ```irq(mode, index)```
* ```set(dest, data)```
* ```nop()```
* ```.side(value)```
* ```.delay(value)```

<FONT COLOR=#BB00FF><font size="5"><b>Clases</font color></font size></b>

* [ ] - class Flash
* [ ] - class PIO
* [ ] class StateMachine

## <FONT COLOR=#007575>**Retardos y cronometrajes**</font>
Este módulo implementa un subconjunto del módulo CPython correspondiente.

El módulo [time](https://docs.micropython.org/en/latest/library/time.html#module-time) proporciona funciones para obtener la hora y fecha actuales, medir intervalos de tiempo, y para generar retardos.

Unix utiliza la fecha estándar de 1970-01-01 00:00:00 UTC para los sistemas POSIX. Sin embargo, algunos puertos embebidos usan el año 2000-01-01 00:00:00 UTC.

Mantener la fecha/hora real del calendario requiere un Reloj en Tiempo Real (RTC). En sistemas con sistema operativo (SO) subyacente (incluyendo algunos RTOS), un RTC puede estar implícito. Establecer y mantener la hora real del calendario es responsabilidad del SO/RTOS y se realiza fuera de MicroPython, sólo utiliza la API del SO para consultar la fecha/hora. La hora actual del calendario puede establecerse usando la función **machine.RTC().datetime(tuple)**, y mantenerse por los siguientes medios:

* Mediante una batería de reserva.
* Mediante protocolo horario en red (requiere configuración por parte de un puerto/usuario).
* Configurado manualmente por un usuario cada vez que se enciende.

Si la hora real del calendario no se mantiene con un sistema/MicroPython RTC, las funciones que vamos a ver a continuación requieren referencia a la hora absoluta actual y pueden no comportarse como se espera.

Uso del módulo [```time```](https://docs.micropython.org/en/latest/library/time.html#module-time):

<div class="cuadrado">

~~~py
import time

time.sleep(1)           # espera 1 segundo
time.sleep_ms(500)      # espera 500 milisegundos
time.sleep_us(100)       # espera 100 microsegundos
start = time.ticks_ms() # obtiene la cuenta en ms
delta = time.ticks_diff(time.ticks_ms(), start) # calcula la diferencia de tiempo
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [time](https://docs.micropython.org/en/latest/library/time.html#module-time). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Funciones</font color></font size></b>

* ```time.gmtime([secs])```
* ```time.localtime([secs])```
* ```time.mktime()```
* ```time.sleep(seconds)```
* ```time.sleep_ms(ms)```
* ```time.sleep_us(us)```
* ```time.ticks_ms()```
* ```time.ticks_us()```
* ```time.ticks_cpu()```
* ```time.ticks_add(ticks, delta)```
* ```time.ticks_diff(ticks1, ticks2)```
* ```time.time()```
* ```time.time_ns()```

## <FONT COLOR=#007575>**Temporizadores**</font>
El temporizador del sistema del RP2040 proporciona una base de tiempo de microsegundos y genera interrupciones para ello. El temporizador por software está disponible en un número ilimitado de ellos (si la memoria lo permite). No hay necesidad de especificar el id del temporizador aunque su valor por defecto (id=-1) es soportado por el momento.

Los temporizadores de hardware se ocupan de la temporización de periodos y eventos. Los temporizadores son quizás la clase de hardware más flexible y heterogénea en MCUs y SoCs, difiriendo enormemente de un modelo a otro. La clase ```Timer``` de **MicroPython** define la operación base de ejecutar un callback con un periodo dado, y permite a placas específicas definir un comportamiento no estándar (que por lo tanto no será portable a otras placas).

Todos los detalles de las funciones están en el módulo [machine.Timer](https://docs.micropython.org/en/latest/library/machine.Timer.html#machine.Timer). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```class machine.Timer(id, /, ...)```. Construye un nuevo objeto temporizador con el ```id``` indicado. Si ```id``` es -1 construye un temporizador virtual (si lo soporta la placa). ```id``` no debe pasarse como argumento.

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```Timer.init(*, mode=Timer.PERIODIC, freq=-1, period=-1, callback=None)```. Con
* [ ] - ```mode``` que puede ser ```Timer.ONE_SHOT``` para que el temporizador se ejecute una vez hasta que expire el periodo configurado del canal; o bien, ```Timer.PERIODIC``` para que el temporizador funcione periódicamente a la frecuencia configurada del canal.
* [ ] - ```freq``` es la frecuencia del temporizador medida en Hz. El límite superior de la frecuencia depende del puerto. Cuando se dan los argumentos ```freq``` y ```period```, ```freq``` tiene mayor prioridad y ```period``` se ignora.
* [ ] - ```period``` es el periodo del temporizador en milisegundos.
* [ ] - ```callback```. La llamada de retorno o ```callback``` debe tomar un argumento, al que se le pasa el objeto ```Timer```. De lo contrario, se producirá una excepción al expirar el temporizador: ```TypeError:'NoneType' object isn't callable```
* ```Timer.deinit()```

<FONT COLOR=#BB00FF><font size="5"><b>Constantes</font color></font size></b>

* ```Timer.ONE_SHOT```
* ```Timer.PERIODIC```

Uso de la clase [```machine.Timer```](https://docs.micropython.org/en/latest/library/machine.Timer.html#machine.Timer):

<div class="cuadrado">

~~~py
from machine import Timer

temp = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
temp.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

## <FONT COLOR=#007575>**Pines y GPIO**</font>
Un objeto pin se utiliza para controlar los pines de E/S (también conocidos como GPIO - entrada/salida de propósito general). Los objetos pin están comúnmente asociados con un pin físico que puede manejar una tensión de salida y leer tensiones de entrada. La clase ```pin``` tiene métodos para establecer el modo del pin (IN, OUT, etc) y métodos para obtener y establecer el nivel lógico digital. Para el control analógico de un pin se utiliza la clase ```ADC```.

Un objeto pin se construye utilizando un identificador que especifica inequívocamente un determinado pin de E/S. Las formas permitidas del identificador y el pin físico al que se asigna el identificador son específicas del puerto. Las posibilidades para el identificador son un entero, una cadena o una tupla con el puerto y el número de pin.

Uso de la clase [```machine.Pin```](https://docs.micropython.org/en/latest/library/machine.Pin.html#machine-pin):

<div class="cuadrado">

~~~py
from machine import Pin

p0 = Pin(0, Pin.OUT)    # crea un pin de salida en GPIO0
p0.on()                 # pone el pin p0 a "on" (nivel alto)
p0.off()                # pone el pin p0 a "off" (nivel bajo)
p0.value(1)             # pone el pin p0 a 1 (nivel alto)

p2 = Pin(2, Pin.IN)     # crea un pin de entrada en el pin GPIO2
print(p2.value())       # obtiene el valor del nivel del pin (0 o 1)

p4 = Pin(4, Pin.IN, Pin.PULL_UP) # habilita la resistencia interna de pull-up
p5 = Pin(5, Pin.OUT, value=1) # pone el pin p5 en estado alto cuando se crea
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.Pin](https://docs.micropython.org/en/latest/library/machine.Pin.html#machine-pin). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```class machine.Pin(id, mode=-1, pull=-1, *, value=None, drive=0, alt=-1)```, donde:

* [ ] ```id``` es la identificación del pin.
* [ ] ```mode``` puede ser ```Pin.IN```, ```Pin.OUT```, ```Pin.OPEN_DRAIN```, ```Pin.ALT```, ```Pin.ALT_OPEN_DRAIN```, ```Pin.ANALOG```
* [ ] ```pull``` puede ser ```None```, ```Pin.PULL_UP```, ```Pin.PUL_DOWN```
* [ ] ```value``` es el valor inicial del pin para ```Pin.OUT``` o ```Pin.OPEN_DRAIN```
* [ ] ```drive``` especifica la potencia de salida de algunos puertos
* [ ] ```alt``` especifica un función alternativa para el pin

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```Pin.init(mode=-1, pull=-1, *, value=None, drive=0, alt=-1)```
* ```Pin.value([x])```
* ```Pin.__call__([x])```
* ```Pin.on()```
* ```Pin.off()```
* ```Pin.irq(handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, *, priority=1, wake=None, hard=False)```
* ```Pin.low()```
* ```Pin.high()```
* ```Pin.mode([mode])```
* ```Pin.pull([pull])```
* ```Pin.drive([drive])```

<FONT COLOR=#BB00FF><font size="5"><b>Constantes</font color></font size></b>

* **Selecciona del modo del pin:** ```Pin.IN```, ```Pin.OUT```, ```Pin.OPEN_DRAIN```, ```Pin.ALT```, ```Pin.ALT_OPEN_DRAIN```, ```Pin.ANALOG```
* **Selecciona si hay una resistencia pull up/down (None para no pull):** ```Pin.PULL_UP```, ```Pin.PULL_DOWN```, ```Pin.PULL_HOLD```
* **Selecciona la potencia de la patilla:** ```Pin.DRIVE_0```, ```Pin.DRIVE_1```, ```Pin.DRIVE_2```
* **Selecciona el tipo de activación IRQ:** ```Pin.IRQ_FALLING```, ```Pin.IRQ_RISING```, ```Pin.IRQ_LOW_LEVEL```, ```Pin.IRQ_HIGH_LEVEL```

## <FONT COLOR=#007575>**Entradas/Salidas programables (PIO)**</font>
PIO es útil para construir interfaces IO de bajo nivel desde cero. En el módulo ```rp2``` se han explicado detalles del lenguaje ensamblador.

Ejemplo usando PIO para hacer parpadear un LED a 1Hz:

<div class="cuadrado">

~~~py
from machine import Pin
import rp2

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink_1hz():
    # Ciclos: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 1)
    set(x, 31)                  [6]
    label("delay_high")
    nop()                       [29]
    jmp(x_dec, "delay_high")

    # Ciclos: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 0)
    set(x, 31)                  [6]
    label("delay_low")
    nop()                       [29]
    jmp(x_dec, "delay_low")

# Crea e inicializa un StateMachine (maquina de estados) con blink_1hz, salida en Pin(25)
sm = rp2.StateMachine(0, blink_1hz, freq=2000, set_base=Pin(25))
sm.active(1)
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

## <FONT COLOR=#007575>**UART (bus serie)**</font>
Hay dos UARTs, UART0 y UART1. UART0 puede asignarse a GPIO 0/1, 12/13 y 16/17, y UART1 a GPIO 4/5 y 8/9.

<div class="cuadrado">

~~~py
from machine import UART, Pin
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart1.write('hola')  # escribe 5 bytes
uart1.read(5) # lee hasta 5 bytes
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.UART](https://docs.micropython.org/en/latest/library/machine.UART.html#machine-uart). Aquí solamente se citan.

UART implementa el protocolo estándar de comunicaciones serie UART/USART. A nivel físico consta de 2 líneas: RX y TX. La unidad de comunicación es un carácter (no confundir con un carácter de cadena) que puede ser de 8 o 9 bits de ancho.

Los objetos UART pueden crearse e inicializarse utilizando:

<div class="cuadrado">

~~~py
from machine import UART

uart = UART(1, 9600)                         # inicializa con la velocidad de transmisión dada
uart.init(9600, bits=8, parity=None, stop=1) # inicializa con los parametros dados
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Los parámetros soportados varían según la placa y para el caso de placas tipo Pyboard, los bits pueden ser 7, 8 o 9. La parada puede ser 1 ó 2. Con ```parity=None```, sólo se soportan 8 y 9 bits. Con ```parity enabled```, sólo se soportan 7 y 8 bits.

Un objeto UART actúa como un objeto stream y la lectura y escritura se realiza utilizando los métodos stream estándar:

<div class="cuadrado">

~~~py
uart.read(10)       # lee 10 caracteres, devuelve un byte
uart.read()         # lee todos los caracteres disponibles
uart.readline()     # lee una línea
uart.readinto(buf)  # lee y almacena en el buffer indicado
uart.write('abc')   # escribe los 3 caracteres
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```class machine.UART(id, ...)```

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```UART.init(baudrate=9600, bits=8, parity=None, stop=1, *, ...)```
* ```UART.deinit()```
* ```UART.any()```
* ```UART.read([nbytes])```
* ```UART.readinto(buf[, nbytes])```
* ```UART.readline()```
* ```UART.write(buf)```
* ```UART.sendbreak()```
* ```UART.irq(trigger, priority=1, handler=None, wake=machine.IDLE)```
* ```UART.flush()```
* ```UART.txdone()```

<FONT COLOR=#BB00FF><font size="5"><b>Constantes</font color></font size></b>

* **Fuentes de disparo IRQ:** UART.RX_ANY

Hay dos UARTs, UART0 y UART1. UART0 puede asignarse a GPIO 0/1, 12/13 y 16/17, y UART1 a GPIO 4/5 y 8/9.

## <FONT COLOR=#007575>**PWM**</font>
Hay 8 generadores PWM independientes llamados slices, cada uno de los cuales tiene dos canales, lo que hace un total de 16 canales PWM que pueden ser sincronizados desde 8Hz hasta 62.5MHz a un ```machine.freq()``` de 125MHz. Los dos canales de un slice funcionan a la misma frecuencia, pero pueden tener una tasa de trabajo diferente. Los dos canales se asignan normalmente a pares de pines GPIO adyacentes con números pares/impares. Así GPIO0 y GPIO1 están en el slice 0, GPIO2 y GPIO3 están en el slice 1, y así sucesivamente. Un determinado canal puede ser asignado a diferentes pines GPIO (ver Pinout). Por ejemplo, el canal A de la sección 0 puede asignarse tanto a GPIO0 como a GPIO16.

Uso la clase ```machine.PWM```:

<div class="cuadrado">

~~~py
from machine import Pin, PWM

# crea un objeto PWM a partir de un pin y establece la frecuencia de
# del slice 0 y el ciclo de trabajo para el canal A
pwm0 = PWM(Pin(0), freq=2000, duty_u16=32768)
pwm0.freq()             # obtiene la frecuencia actual del slice 0
pwm0.freq(1000)         # establece/cambia la frecuencia actual del slice 0
pwm0.duty_u16()         # obtiene el ciclo de trabajo actual del canal A, rango 0-65535
pwm0.duty_u16(200)      # establece el ciclo de trabajo del canal A, rango 0-65535
pwm0.duty_u16(0)        # detiene la salida en el canal A
print(pwm0)             # muestra las propiedades del objeto PWM
pwm0.deinit()           # apaga el PWM del slice 0, parando los canales A y B
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

## <FONT COLOR=#007575>**ADC**</font>
El RP2040 tiene cinco canales ADC (conversión analógica a digital) en total, cuatro de los cuales son ADC basados en SAR (registro de aproximación sucesiva) de 12 bits: GP26, GP27, GP28 y GP29. La señal de entrada para ADC0, ADC1, ADC2 y ADC3 se puede conectar con GP26, GP27, GP28, GP29 respectivamente (en la placa Pico, GP29 está conectado a VSYS). El rango estándar del ADC es de 0-3,3 V. El quinto canal está conectado al sensor de temperatura incorporado y puede utilizarse para medir la temperatura.

Uso de la clase machine.ADC:

<div class="cuadrado">

~~~py
from machine import ADC, Pin
adc = ADC(Pin(26))     # crea un objeto adc en un pin ADC
adc.read_u16()         # lee el valor (0-65535) a través del rango de tensión 0.0v - 3.3v
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

La clase ADC proporciona una interfaz para los convertidores analógico-digitales, y representa finalmente que puede muestrear una tensión continua y convertirla en un valor discretizado.

Ejemplo de uso:

<div class="cuadrado">

~~~py
from machine import ADC

adc = ADC(pin)        # create un objeto adc en un pin
val = adc.read_u16()  # lee un valor analogico en el rango 0-65535
val = adc.read_uv()   # lee un valor analogico en microvoltios
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.ADC](https://docs.micropython.org/en/latest/library/machine.ADC.html#machine-adc). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```class machine.ADC(id, *, sample_ns, atten)```, donde ```sample_ns``` es el tiempo de muestreo en nanosegundos y ```atten``` especifica la atenuación de entrada.

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```ADC.init(*, sample_ns, atten)```
* ```ADC.block()```
* ```ADC.read_u16()```
* ```ADC.read_uv()```

## <FONT COLOR=#007575>**Bus SPI**</font>

### <FONT COLOR=#AA0000>Software</font>
El software SPI (usando bit-banging) funciona en todos los pines, y se accede a través de la clase ```machine.SoftSPI```:

<div class="cuadrado">

~~~py
from machine import Pin, SoftSPI

# construye un bus SoftSPI en los pines indicados
# polaridad en el estado de reposo de SCK
# phase=0 indica el primer flanco de SCK, phase=1 significa el segundo
spi = SoftSPI(baudrate=100_000, polarity=1, phase=0, sck=Pin(0), mosi=Pin(2), miso=Pin(4))

spi.init(baudrate=200000) # establece la velocidad de transmision o baudrate

spi.read(10)            # lee 10 bytes de MISO
spi.read(10, 0xff)      # lee 10 bytes mientras emite 0xff en MOSI

buf = bytearray(50)     # crea un buffer
spi.readinto(buf)       # lee en el buffer indicado (lee 50 bytes en este caso)
spi.readinto(buf, 0xff) # lee en el buffer indicado mientras emite 0xff en MOSI

spi.write(b'12345')     # escribe 5 bytes en MOSI

buf = bytearray(4)      # crea un buffer
spi.write_readinto(b'1234', buf) # escribe en MOSI y lee de MISO en el buffer
spi.write_readinto(buf, buf) # escribe buf en MOSI y lee MISO en buf
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

El bit-banging es un proceso en el que se emula un periférico no disponible utilizando comandos directos de manipulación de puertos en los pines GPIO.

SPI es un protocolo serie síncrono manejado por un controlador. A nivel físico, un bus consta de 3 líneas: SCK, MOSI, MISO. Varios dispositivos pueden compartir el mismo bus. Cada dispositivo debe tener una señal separada, CS (Chip Select), para seleccionar un dispositivo concreto en un bus con el que se produce la comunicación. La gestión de una señal CS debe realizarse en código de usuario (a través de la clase ```machine.Pin```).

Existen implementaciones de SPI tanto por hardware como por software a través de las clases ```machine.SPI``` y ```machine.SoftSPI```. El hardware SPI utiliza el soporte de hardware del sistema para realizar las lecturas/escrituras y es normalmente eficiente y rápido pero puede tener restricciones en los pines que pueden ser utilizados. Software SPI es implementado por bit-banging y puede ser usado en cualquier pin pero no es tan eficiente. Estas clases tienen los mismos métodos disponibles y difieren principalmente en la forma en que se construyen.

Todos los detalles de las funciones están en el módulo [machine.SoftSPI](https://docs.micropython.org/en/latest/library/machine.SPI.html#machine-softspi). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructores</font color></font size></b>

* ```class machine.SPI(id, ...)```
* ```class machine.SoftSPI(baudrate=500000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None)```

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```SPI.init(baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO))```
* ```SPI.deinit()```
* ```SPI.read(nbytes, write=0x00)```
* ```SPI.readinto(buf, write=0x00)```
* ```SPI.write(buf)```
* ```SPI.write_readinto(write_buf, read_buf)```

<FONT COLOR=#BB00FF><font size="5"><b>Constantes</font color></font size></b>

* **Para inicializar el controlador del bus SPI:** ```SPI.CONTROLLER```
* **Establecer el primer bit como bit mas significativo:** ```SPI.MSB```, ```SoftSPI.MSB```
* **Establecer el primer bit como bit menos significativo:** ```SPI.LSB```, ```SoftSPI.LSB```

### <FONT COLOR=#AA0000>Hardware</font>
El RP2040 tiene 2 buses hardware SPI a los que se accede a través de la clase ```machine.SPI``` y tiene los mismos métodos que el software SPI visto antes:

<div class="cuadrado">

~~~py
from machine import Pin, SPI

spi = SPI(1, 10_000_000)  # Asignacion por defectdo: sck=Pin(10), mosi=Pin(11), miso=Pin(8)
spi = SPI(1, 10_000_000, sck=Pin(14), mosi=Pin(15), miso=Pin(12))
spi = SPI(0, baudrate=80_000_000, polarity=0, phase=0, bits=8, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

## <FONT COLOR=#007575>**Bus I2C**</font>
I2C es un protocolo de dos hilos para la comunicación entre dispositivos. A nivel físico consta de 2 hilos: SCL y SDA que son las líneas de reloj y datos respectivamente.

Los objetos I2C se crean en un bus específico. Pueden inicializarse cuando se crean, o inicializarse más tarde.

Al imprimir el objeto I2C se obtiene información sobre su configuración.

Existen implementaciones de I2C tanto por hardware como por software a través de las clases ```machine.I2C``` y ```machine.SoftI2C```. El hardware I2C utiliza el soporte hardware del sistema para realizar las lecturas/escrituras y suele ser eficiente y rápido, pero puede tener restricciones en cuanto a los pines que se pueden utilizar. Software I2C es implementado por bit-banging y puede ser usado en cualquier pin pero no es tan eficiente. Estas clases tienen los mismos métodos disponibles y difieren principalmente en la forma en que se construyen.

El bus I2C requiere resistencias de pull-up tanto en SDA como en SCL para su funcionamiento. Normalmente son resistencias en el rango de 1 a 10 K, conectadas desde cada SDA/SCL a Vcc. Sin ellas, el comportamiento es indefinido y puede ir desde el bloqueo, reset inesperado del watchdog o simplemente valores erróneos. A menudo, este circuito de pull-up ya está incorporado en la placa MCU o en las placas de sensores, pero no hay ninguna regla al respecto, por lo que debemos comprobarlo en caso de problemas.

Ejemplo de uso:

<div class="cuadrado">

~~~py
from machine import I2C

i2c = I2C(freq=400000)          # crear periférico I2C a una frecuencia de 400kHz
                                # dependiendo del puerto, pueden ser necesarios parámetros adicionales
                                # para seleccionar el periférico y/o los pines a utilizar

i2c.scan()                      # buscar periféricos, devolviendo una lista de direcciones de 7 bits

i2c.writeto(42, b'123')         # escribir 3 bytes en el periférico con dirección de 7 bits 42
i2c.readfrom(42, 4)             # leer 4 bytes del periférico con dirección de 7 bits 42

i2c.readfrom_mem(42, 8, 3)      # leer 3 bytes de la memoria del periférico 42, comenzando en la 
                                # dirección de memoria 8 del periférico
i2c.writeto_mem(42, 2, b'\x10') # escribir 1 byte en la memoria del periférico 42, comenzando en la 
                                # dirección 2 del periférico
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

### <FONT COLOR=#AA0000>Software</font>
Software I2C (usando bit-banging) funciona en todos los pines con capacidad de salida, y se accede a través de la clase ```machine.SoftI2C```:

<div class="cuadrado">

~~~py
from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100_000)

i2c.scan()              # búsqueda de dispositivos

i2c.readfrom(0x3a, 4)   # leer 4 bytes del dispositivo con dirección 0x3a
i2c.writeto(0x3a, '12') # escribe '12' en dispositivo con dirección 0x3a

buf = bytearray(10)     # crea un buffer con 10 bytes
i2c.writeto(0x3a, buf)  # escribir el búfer en el periférico
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.SoftI2C](https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-softi2c). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```classmachine.I2C(id, *, scl, sda, freq=400000, timeout=50000)```

Los métodos son los mismos que en vemos en hardware.

### <FONT COLOR=#AA0000>Hardware</font>
Se accede al controlador a través de la clase ```machine.I2C```.

<div class="cuadrado">

~~~py
from machine import Pin, I2C

i2c = I2C(0)   # default assignment: scl=Pin(9), sda=Pin(8)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400_000)
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.I2C](https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```classmachine.SoftI2C(scl, sda, *, freq=400000, timeout=50000)```

<FONT COLOR=#BB00FF><font size="5"><b>Métodos generales</font color></font size></b>

* ```I2C.init(scl, sda, *, freq=400000)```
* ```I2C.deinit()```
* ```I2C.scan()```

<FONT COLOR=#BB00FF><font size="5"><b>Operaciones primitivas I2C</font color></font size></b>

Los siguientes métodos implementan las operaciones primitivas del bus controlador I2C y pueden combinarse para realizar cualquier transacción I2C. Se proporcionan si se necesita más control sobre el bus, de lo contrario se pueden utilizar los métodos estándar.

* ```I2C.start()```
* ```I2C.stop()```
* ```I2C.readinto(buf, nack=True, /)```
* ```I2C.write(buf)```

<FONT COLOR=#BB00FF><font size="5"><b>Operaciones estándar del bus</font color></font size></b>

Los siguientes métodos implementan las operaciones estándar de lectura y escritura del controlador I2C dirigidas a un dispositivo periférico determinado.

* ```I2C.readfrom(addr, nbytes, stop=True, /)```
* ```I2C.readfrom_into(addr, buf, stop=True, /)```
* ```I2C.writeto(addr, buf, stop=True, /)```
* ```I2C.writevto(addr, vector, stop=True, /)```

<FONT COLOR=#BB00FF><font size="5"><b>Operadores con memoria</font color></font size></b>

Algunos dispositivos I2C actúan como un dispositivo de memoria (o conjunto de registros) desde el que se puede leer y en el que se puede escribir. En este caso hay dos direcciones asociadas con una transacción I2C: la dirección del periférico y la dirección de la memoria. Los siguientes métodos son funciones para comunicarse con tales dispositivos.

* ```I2C.readfrom_mem(addr, memaddr, nbytes, *, addrsize=8)```
* ```I2C.readfrom_mem_into(addr, memaddr, buf, *, addrsize=8)```
* ```I2C.writeto_mem(addr, memaddr, buf, *, addrsize=8)```

## <FONT COLOR=#007575>**Bus I2S**</font>
I2S es un protocolo serie síncrono utilizado para conectar dispositivos de audio digital. A nivel físico, un bus consta de 3 líneas: SCK, WS, SD. La clase I2S admite el funcionamiento de controlador. El funcionamiento periférico no está soportado.

Los objetos I2S pueden crearse e inicializarse utilizando:

<div class="cuadrado">

~~~py
from machine import I2S
from machine import Pin

# ESP32
sck_pin = Pin(14)   # Salida de reloj serie
ws_pin = Pin(13)    # Salida de reloj
sd_pin = Pin(12)    # Salida de datos serie

or

# PyBoards
sck_pin = Pin("Y6")   # Salida de reloj serie
ws_pin = Pin("Y5")    # Salida de reloj
sd_pin = Pin("Y8")    # Salida de datos serie

audio_out = I2S(2,
                sck=sck_pin, ws=ws_pin, sd=sd_pin,
                mode=I2S.TX,
                bits=16,
                format=I2S.MONO,
                rate=44100,
                ibuf=20000)

audio_in = I2S(2,
               sck=sck_pin, ws=ws_pin, sd=sd_pin,
               mode=I2S.RX,
               bits=32,
               format=I2S.STEREO,
               rate=22050,
               ibuf=20000)
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Están soportados tres modos de operación:

* **blocking:**

<div class="cuadrado">

~~~py
num_written = audio_out.write(buf) # bloques hasta vaciar buf

num_read = audio_in.readinto(buf) # bloquea hasta llenar buf
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

* **non-blocking:**

<div class="cuadrado">

~~~py
audio_out.irq(i2s_callback)          # i2s_callback es llamado cuando buf se vacía
num_written = audio_out.write(buf)   # retorna inmediatamente

audio_in.irq(i2s_callback)           # i2s_callback es llamado cuando buf se vacía
num_read = audio_in.readinto(buf)    # retorna inmediatamente
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

* **asyncio:**

<div class="cuadrado">

~~~py
swriter = asyncio.StreamWriter(audio_out)
swriter.write(buf)
await swriter.drain()

sreader = asyncio.StreamReader(audio_in)
num_read = await sreader.readinto(buf)
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.I2S](https://docs.micropython.org/en/latest/library/machine.I2S.html#machine-i2s). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```classmachine.I2S(id, *, sck, ws, sd, mck=None, mode, bits, format, rate, ibuf)```

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```I2S.init(sck, ...)```
* ```I2S.deinit()```
* ```I2S.readinto(buf)```
* ```I2S.write(buf)```
* ```I2S.irq(handler)```
* ```staticI2S.shift(*, buf, bits, shift)```

<FONT COLOR=#BB00FF><font size="5"><b>Constantes</font color></font size></b>

* ```I2S.RX¶```
* ```I2S.TX```
* ```I2S.STEREO```
* ```I2S.MONO```

<div class="cuadrado">

~~~py
from machine import I2S, Pin

i2s = I2S(0, sck=Pin(16), ws=Pin(17), sd=Pin(18), mode=I2S.TX, bits=16, format=I2S.STEREO, rate=44100, ibuf=40000) # crea objeto I2S
i2s.write(buf)             # escribir búfer de muestras de audio en el dispositivo I2S

i2s = I2S(1, sck=Pin(0), ws=Pin(1), sd=Pin(2), mode=I2S.RX, bits=16, format=I2S.MONO, rate=22050, ibuf=40000) # crea objeto I2S
i2s.readinto(buf)          # llena el búfer con muestras de audio del dispositivo I2S
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

## <FONT COLOR=#007575>**Reloj en tiempo real (RTC)**</font>
El RTC es un reloj independiente que controla la fecha y la hora.

Ejemplo de uso:

<div class="cuadrado">

~~~py
rtc = machine.RTC()
rtc.datetime((2020, 1, 21, 2, 10, 32, 36, 0))
print(rtc.datetime())
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.RTC](https://docs.micropython.org/en/latest/library/machine.RTC.html#machine-rtc). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```classmachine.RTC(id=0, ...)```

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```RTC.datetime([datetimetuple])```
* ```RTC.init(datetime)```
* ```RTC.now()```
* ```RTC.deinit()```
* ```RTC.alarm(id, time, *, repeat=False)```
* ```RTC.alarm_left(alarm_id=0)```
* ```RTC.cancel(alarm_id=0)```
* ```RTC.irq(*, trigger, handler=None, wake=machine.IDLE)```

<FONT COLOR=#BB00FF><font size="5"><b>Constantes</font color></font size></b>

* ```RTC.ALARM0```

<div class="cuadrado">

~~~py
from machine import RTC

rtc = RTC()
rtc.datetime((2017, 8, 23, 2, 12, 48, 0, 0)) # establece fecha y hora
                                             # por ejemplo 2023/11/10 16:12:48
rtc.datetime() # obtiene fecha y hora
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

## <FONT COLOR=#007575>**Temporizador WDT (Watchdog)**</font>
El RP2040 tiene un watchdog que es un temporizador de cuenta atrás que puede reiniciar partes del chip si llega a cero.

El WDT se utiliza para reiniciar el sistema cuando la aplicación se bloquea y termina en un estado no recuperable. Una vez iniciado no puede ser detenido o reconfigurado de ninguna manera. Después de habilitarlo, la aplicación debe "alimentar" al watchdog periódicamente para evitar que expire y reinicie el sistema.

Ejemplo de uso:

<div class="cuadrado">

~~~py
from machine import WDT
wdt = WDT(timeout=2000)  # habilitarlo con un tiempo de espera de 2s
wdt.feed()
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Todos los detalles de las funciones están en el módulo [machine.WDT](https://docs.micropython.org/en/latest/library/machine.WDT.html#machine-wdt). Aquí solamente se citan.

<FONT COLOR=#BB00FF><font size="5"><b>Constructor</font color></font size></b>

* ```classmachine.WDT(id=0, timeout=5000)```

<FONT COLOR=#BB00FF><font size="5"><b>Métodos</font color></font size></b>

* ```WDT.feed()```

<div class="cuadrado">

~~~py
from machine import WDT

# activar el WDT con un tiempo de espera de 5s (1s es el mínimo)
wdt = WDT(timeout=5000)
wdt.feed()
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

## <FONT COLOR=#007575>**Drive un hilo (OneWire)**</font>
El controlador OneWire está implementado en software y funciona en todos los pines:

<div class="cuadrado">

~~~py
from machine import Pin
import onewire

ow = onewire.OneWire(Pin(12)) # crear un bus OneWire en GPIO12
ow.scan()               # devuelve una lista de dispositivos en el bus
ow.reset()              # reset del bus
ow.readbyte()           # lee un byte
ow.writebyte(0x12)      # escribe un byte en el bus
ow.write('123')         # escribe bytes en el bus
ow.select_rom(b'12345678') # seleccionar un dispositivo específico por su código ROM
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Existe un controlador específico para los dispositivos DS18S20 y DS18B20:

<div class="cuadrado">

~~~py
import time, ds18x20
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
ds.convert_temp()
time.sleep_ms(750)
for rom in roms:
    print(ds.read_temp(rom))
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

Hay que asegurarse de poner una resistencia pull-up de 4.7k en la línea de datos. Tengase en cuenta que el método ```convert_temp()``` debe ser llamado cada vez que desee muestrear la temperatura.

## <FONT COLOR=#007575>**NeoPixel y driver APA106**</font>
Uso de los módulos ```neopixel``` y ```apa106```:

<div class="cuadrado">

~~~py
from machine import Pin
from neopixel import NeoPixel

pin = Pin(0, Pin.OUT)   # pone GPIO0 como salida para el drive NeoPixels
np = NeoPixel(pin, 8)   # crea el drive NeoPixel en GPIO0 para 8 pixels
np[0] = (255, 255, 255) # pone el pixel 0 (primero) a blanco
np.write()              # escribe datos en todos los pixeles
r, g, b = np[0]         # obtiene el color del primer pixel
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>

El controlador APA106 extiende NeoPixel, pero internamente utiliza un orden de colores diferente:

<div class="cuadrado">

~~~py
from apa106 import APA106
ap = APA106(pin, 8)
r, g, b = ap[0]
~~~

</div>
<style>
.cuadrado{
padding:5px;
margin:5px;
background-color: #FFFFDD;
border: solid 2px #FFFFA0;
color: black;
}
</style>
