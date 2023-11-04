# <FONT COLOR=#8B008B>Permisos en Linux</font>
Aunque no es un tema de Python si es muy probable que necesitemos en algún momento cambiar los permisos de un directorio o de un archivo y por eso dejo aquí esta pequeña guía.

## <FONT COLOR=#007575>**Tipos de permisos en Linux**</font>
El comando CHMOD nos da la posibilidad de poder cambiar los permisos de los archivos y directorios combinando entre clases y tipos. Hay cuatro clases:

* Propietario (u). Creador del archivo o la carpeta
* Grupo (g). Usuarios que tendrán acceso al archivo o carpeta
* Otros (o). Todos los usuarios
* Todos (a). Todos los tipos de usuario (propietario, grupo y otros)

Hay tres tipos de permisos:

* Lectura ( r). Permite que el usuario vea el archivo pero no puede realizar cambios en el mismo ni copiarlo o borrarlo.
* Escritura (w). Se permite que los usuarios que acceden al archivo o carpeta puedan realizar sobre el mismo cualquier tipo de edición, copiar, cortar o borrar.
* Ejecutar (x). Al activar esta opción, la cual viene por defecto deshabilitada, podemos ejecutar archivos.

Hay tres modificadores para la tarea:

* +. Concede el permiso
* -. Deniega el permiso
* =. Sobreescribe un permiso con el permiso anterior.

En entornos Unix cada permiso tiene el siguiente valor:

* Lectura: 4
* Escritura: 2
* Ejecución: 1

## <FONT COLOR=#007575>**Trabajar con permisos**</font>
Jugando con sumas de estos valores establecemos distintos permisos, por ejemplo, si queremos dar un permiso de escritura usaremos el 6 = 4 + 2 (Lectura + Escritura). Si queremos que pueda ejecutar usaremos el 7 = 4 + 2 + 1 (Lectura + Escritura + Ejecución).

En la tabla tenemos todos los valores posibles.

<center>

|**Dec.**|**Bin.**|**Permiso**|**read**|**write**|**exe**|
|:-:|:-:|---|:-:|:-:|:-:|
|0|000|Sin permisos|N|N|N|
|1|001|Ejecución|N|N|Y|
|2|010|Escritura|N|Y|N|
|3|011|Lectura y escritura|N|Y|Y|
|4|100|Lectura|Y|N|N|
|5|101|Lectura y ejecución|Y|N|Y|
|6|110|Lectura y escritura|Y|Y|N|
|7|111|Lectura, escritura y ejecución|Y|Y|Y|

</center>

El procedimiento para establecer el permiso es muy sencillo. Basta con ir a una terminal y ejecutar la siguiente orden:

~~~
chmod Tipo-permiso Ruta-Archivo
~~~

Ejemplos para modificar permisos en modo terminal:

~~~
chmod o=rwx * → Dar permisos de lectura, escritura y ejecución a los otros usuarios.

chmod go= * → Quitar todos los permisos a grupo y los otros usuarios.

chmod 666 /Documentos/curso-python/Ejercicios/holamundo.py
~~~

En sistemas Linux con letras veremos algo como lo siguiente:

* 0 → ---  → sin acceso
* 1 → --x → ejecución
* 2 → -w- → escritura
* 3 → -wx → escritura y ejecución
* 4 → r-- → lectura
* 5 → r-x → lectura y ejecución
* 6 → rw- → lectura y escritura
* 7 → rwx → lectura, escritura y ejecución

Por ejemplo: *chmod 777*. Le damos a los 3 tipos de usuarios permiso de lectura, ejecución y escritura (hemos sumado4+2+1).  Si queremos dar permisos de lectura y escritura sería 4+2 = 6 y si si lo que queremos es sólo dar lectura sería 4. Si lo que queremos es dar lectura y ejecución sería de sumar 4 + 1 = 5.

Diferentes combinaciones típicas:

* *chmod 755*. Permiso de lectura y ejecución (4+1) a todos los usuarios excepto al propietario que lo tiene completo (lectura, escritura, ejecución 4+2+1).
* *chmod 666*. Permisos de lectura y escritura a todos, excepto ejecución (4+2). Todos pueden acceder al archivo, leer su contenido y modificarlo.
* *chmod 644*. Se suele utilizar para no permitr la escritura a nadie que no sea el propietario. El 755 es similar, lectura y ejecución aunque este es más restrictivo (sólo lectura) y (lectura, escritura para propietario).
