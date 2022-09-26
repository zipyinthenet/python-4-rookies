# CURSO python3
## Python 4 rookies

### INDICE
### [1. Primer acercamiento al Scripting](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#1-primer-acercamiento-al-scripting)

### [2. Acerca de Python](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#2-acerca-de-python)

### [3. Elementos del Lenguaje](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#3-elementos-del-lenguaje)

### [4. Codificacion de caracteres](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#4-codificacion-de-caracteres)

### [5. Tipos de datos complejos](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#5-tipos-de-datos-complejos)

### [6. Estructuras de Control de Flujo](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#6-estructuras-de-control-de-flujo)

### [7. Funciones](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#7-funciones)

### [8. Inyeccion de variables](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#8-inyeccion-de-variables)

### [9. Importacion de modulos](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#9-importacion-de-modulos)

### [10. Metodos de manipulacion de variables](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#10-metodos-de-manipulacion-de-variables)

### [11. Manipulacion de cadenas de texto](http://192.168.0.150:8088/ruben/python_para_principiantes/src/branch/master#11-manipulacion-de-cadenas-de-texto)

### 12. Manipulacion de listas y tuplas

### 13. Manipulacion de diccionarios

### 14. Manejo y manipulación de archivos

### 15. Manejo de archivos CSV

### 16. Manipulación avanzada de cadenas de texto

### 17. Creando menus de opciones

### 18. Generacion de registros de sistema

### 19. Modulos del sistema(os, sys y subprocess)

### 20. Conexiones remotas (HTTP, FTP y SSH)

### 21. Bibliotecas para el Manejo avanzado de archivos, en sistemas GNU/LINUX

### 22. Probabilidad y Estadistica con Python

### 23. Estadistica descriptiva con Python

### 24. Python como CGI para aplicaciones Web

### 25. Conexiones a bases de datos con MySQL y MariaDB

### 26. Programación orientada a objetos con Python

### 1. Primer acercamiento al Scripting

Archivo ejecutable
```python
chmod +x nombre-del-archivo
```

Lenguaje interpretado
Interprete en la primera linea , ejemplos:
```python
#!/usr/bin/env python
#!/usr/bin/env python2
#!/usr/bin/env python3
#!/usr/bin/env bash
```

Ejemplo script:
```python
#!/usr/bin/env python3
print("Hola Mundo!")
```

### 2. Acerca de Python

...

### 3. Elementos del Lenguaje

#### Variables
```python
#!/usr/bin/env python3
nombre_de_la_variable = valor_de_la_variable
```

```python
#!/usr/bin/env python3
variable = 12
```

#### Entrada y Salida

```python
#!/usr/bin/env python3
mi_variable = 15
print(mi_variable)
```

```python
#!/usr/bin/env python3
mi_variable = input("Ingresa un valor: ")
print(mi_variable)
```

#### Tipos de datos

Cadena de texto (string):
```python
#!/usr/bin/env python3
mi_cadena = "Hola mundo!"
otra_cadena = 'Hola mundo!'
```

```python
#!/usr/bin/env python3
mi_cadena_multilinea = """
Esta es una Cadena
de varias lineas
"""
```

Numero entero:
```python
#!/usr/bin/env python3
edad = 25
```

Numero real:
```python
#!/usr/bin/env python3
precio = 35.05
```

Booleano(verdadero/falso):
```python
#!/usr/bin/env python3
verdadero = True
falso = False
```

#### Operadores Aritmeticos

Suma
```python
#!/usr/bin/env python3
a = 10 + 5
```

Resta
```python
#!/usr/bin/env python3
a = 12 - 7
```

Negacion
```python
#!/usr/bin/env python3
a = -5
```

Multiplicacion
```python
#!/usr/bin/env python3
a = 7 * 5
```

Exponente
```python
#!/usr/bin/env python3
a = 2 ** 3
```

Division
```python
#!/usr/bin/env python3
a = 12.5 / 2
```

Division entera
```python
#!/usr/bin/env python3
a = 12.5 // 2
```

Modulo
```python
#!/usr/bin/env python3
a = 27 % 4
```

#### Comentarios

Comentario en una sola linea
```python
#!/usr/bin/env python3
# Comentario en una linea
```

Comentario de varias lineas
```python
#!/usr/bin/env python3
"""Y esto es un comentario
de varias lineas"""
```

Comentario en lineas
```python
#!/usr/bin/env python3
mi_variable = 15  # comentario en linea
```

### 4. Codificacion de caracteres

Esta declaracion es opcional desde la version 3.0 :
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
variable = "En el mundo Ñagara encontré un Ñandú"
```

### 5. Tipos de datos complejos

#### Tuplas

Tupla es una variable que permite almacenar datos inmutables

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_tupla[1])  # Salida: 15
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_tupla[1:4])  # Devuelve: (15, 2.8, 'otro dato')
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_tupla[3:])  # Devuelve: ('otro dato', 25)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_tupla[:2])  # Devuelve: ('cadena de texto', 15)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_tupla[-1])  # Salida: 25
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_tupla[-2])  # Salida: otro dato
```

#### Listas

Lista es similar a la tupla , solo que en la lista , SI esta permitido modificar datos

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_lista[1])  # Salida: 15
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_lista[1:4])  # Devuelve: [15, 2.8, 'otro dato']
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(mi_lista[-2])  # Salida: otro dato
```

Los datos de una lista , NO son inmutables , pero SI modificables , una vez creados

Declarar nuevo valor , posicion 2:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_lista[2] = 3.8
print(mi_lista[2])  # Salida: 3.8 , el tercer elemento ahora es 3.8
```

Tambien se permiten añadir nuevos datos a las listas:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_lista.append('Nuevo Dato')
print(mi_lista)  # Salida: 'cadena de texto', 15, 2.8, 'otro dato', 25, 'Nuevo Dato'
```

#### Diccionarios

Los Diccionarios , como las tuplas y listas , son colecciones.
En un diccionario , la posicion del dato se asocia a un valor.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_diccionario = {
    'clave_1': valor_1,
    'clave_2': valor_2,
    'clave_7': valor_7
}
print(mi_diccionario['clave_2'])  # Salida: valor_2
```

Borrar cualquier entrada de un diccionario:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
del(mi_diccionario['clave_2'])
```

Modificar valores en diccionario , como en las listas:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_diccionario['clave_1'] = 'Nuevo valor'
```

Agregar mas elementos al diccionario , con mas valores en sus claves:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_diccionario['nueva_clave'] = 'Nuevo elemento'
```

### 6. Estructuras de Control de Flujo

Como agrupar instrucciones de forma controlada

- Estructuras de control condicionales
- Estructuras de control iterativas

#### Sangrado

Sangrado en python es obligatorio.

Sangrado 4 espacios en blanco , indicara que las instrucciones forman parte de una misma estructura de control

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
inicio de la estructura de control:
    expresiones
```

#### Estructuras de control de flujo condicionales

Las condiciones se evaluan como verdaderas o falsas.

- se utilizan operadores relacionales o de comparacion

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'==' igual que
'!=' distinto que
'<' menor que
'>' mayor que
'<=' menor o igual que
'>=' mayor o igual que
```

- operadores logicos

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
and (y)
5 == 7 and 7 < 12 0y0 falso
9 < 12 and 12 > 7 1y1 verdadero
9 < 12 and 12 > 15 1y0 falso

or (o)
12 == 12 or 15 < 7 1o0 verdadero
7 > 5 or 9 < 12 1o1 verdadero
```

Definicion estructura de control de flujo condicional:

if (si) , elif (sino, si) , else (sino)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if gasto <= 100:
    pagar_en_efectivo()
elif gasto > 100 and gasto < 300:
    pagar_con_debito()
else:
    pagar_con_credito()
```

#### Estructuras de control iterativas

Python dispone de 2 estructuras de control iterativas:

- bucle while
- bucle for

##### Bucle while

**mientras** que una condicion se cumpla se encarga de ejecutar una misma accion:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
year = 2016

while year <= 2022:
    print("Informes de", year)
    year +=1
```
Informes de 2016  

Informes de 2017  

Informes de 2018  

Informes de 2019

Informes de 2020

Informes de 2021

Informes de 2022  

Instruccion break:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    nombre = raw_input("Indique su nombre: ")
    if nombre:
        break
```
En caso de que la variable sea verdadera , break se ejecutara.

##### Bucle for

El bucle siempre se utiliza sobre una tupla o una lista.

Por cada elemento de la lista se ejecutaran mismas acciones:

En cada elemento mi_lista , imprimir el elemento:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Ana']
for elemento in mi_lista:
    print(elemento)
```

En cada elemento mi_tupla , imprimir color:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
mi_tupla = ['rosa', 'verde', 'celeste', 'amarillo']
for color in mi_tupla:
    print(color)
```

Emular a while:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for year in range(2011, 2023):
    print("Informes de", year)
```

### 7. Funciones

Una Funcion alberga expresiones y algoritmos que son ejecutados cuando se invoca una funciona ya definida.

El propio lenguaje de Python contiene funciones incorporadas , pero el usuario tambien puede definir nuevas.

#### Funciones definidas por el usuario

En Python para definir funciones se utiliza la instruccion 'def' mas un nombre de la funcion.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion():
  print("Hola")  # aqui el algoritmo identado
```

Una funcion no funciona hasta que no es invocada:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion():
  return "Hola"  # aqui el algoritmo identado
mi_funcion()
```

El valor de una funcion puede almacenarse en una variable:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion():
  return "Hola"  # aqui el algoritmo identado
palabra = mi_funcion()
```

El valor de una funcion puede imprimirse en una variable:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion():
  return "Hola"  # aqui el algoritmo identado
palabra = mi_funcion()
print(palabra)
```

El valor de una funcion puede ignorarse en una variable:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion():
  return "Hola"  # aqui el algoritmo identado
mi_funcion()
```

#### Sobre los parametros

un parametro es un valor de la funcion , se definen entre los parentesis y separados por coma.

instruccion 'pass' se utiliza para completar una estructura de control que no realiza ninguna accion.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion(param1, param2):
    pass
```

Los parametros de una funcion seran utilizados dentro de su algoritmos

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion(patatas, tomates):
    sumadevegetables = patatas + tomates
    return sumadevegetables
mi_funcion(5, 5)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mi_funcion(patatas, tomates):
    sumadevegetables = patatas + tomates
    print(sumadevegetables)
mi_funcion(5, 5)
```

#### Parametros por omision

Es posible asignar valores estaticos o por defecto a los parametros en las funciones.
La definicion de una funcion la deben anteceder dos lineas en blanco.
El valor parametro por omision no se debe dejar ningun espacio ni antes ni despues signo '='
El parametro por omision se define SIEMPRE a continuacion de definir primero los obligatorios
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mi_funcion(patatas, tomates=10):
    sumadevegetables = patatas + tomates
    print(sumadevegetables)

mi_funcion(5)
```

#### Claves como argumentos

las claves como argumentos , Python permite llamar a una funcion pasandole argumentos esperados como pares claves=valor

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funcion(obligatorio1, opcional='valor por defecto', opcional_dos=15):
    pass
funcion('valor obligatorio', opcional_dos=43)
```

#### Parametros arbitrarios

para definir argumentos arbitrarios en una funcion , se antecede un asterisco *
los argumentos arbitrarios preceden(van despues) de los obligatorios
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funcion(obligatorio, *arbitrarios):
    pass
funcion('fijo', 1, 2, 3, 4, 5)
funcion('fijo', 1, 2)
funcion('fijo', 1, 2, 3, 4, 5, 6, 7)
funcion('fijo')
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funcion(*arbitrarios):
    for argumento in arbitrarios:
        valor = arbitrarios[argumento]
        print(valor)
funcion(1, 2)        
```

es posible definir argumentos arbitrarios como pares de clave=valor , al nombre del parametro deben precederlo dos asteriscos (**):

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funcion(obligatorio, **arbitrarios):
    pass
funcion('fijo', a=1, b=2, c=3)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funcion(**arbitrarios):
    for argumento in arbitrarios:
        valor = arbitrarios[argumento]
        print(valor)
funcion(a=1, b=2)
```

#### Desempaquetado de parametros

Se pueden definir los parametros de la funcion , en forma de lista o de diccionario,
y estos pasarlos a la funcion:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funcion(uno, dos, tres):
    pass
# DESEMPAQUETADO DE LISTAS
parametros = [1, 2, 3]
funcion(*parametros)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funcion(uno, dos, tres):
    pass
# DESEMPAQUETADO DE LISTAS
parametros = dict(uno=1, dos=2, tres=3)
funcion(**parametros)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def funcion(uno, dos, tres):
    pass


# DESEMPAQUETADO DE LISTAS
parametros = {'uno': 1, 'dos': 2, 'tres': 3}
funcion(**parametros)
```

#### Llamadas recursivas y de retorno

Una funcion puede llamar a otro funcion que retorne un valor

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def retornar(algo):
    return str(algo)


def llamar():
    algo = retornar()
```

La llamada interna se puede almacenar , retornar o ignorarse

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def almacenar():
    algo = retornar()


def volver_a_retornar():
    return retornar()


def ignorar():
    retornar()
```

llamada recursiva , es cuando se define la funcion y la llamada que se hace es a la misma funcion.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_nombre():
    nombre = raw_input("Nombre: ")
    if not nombre:
        get_nombre()
```

#### Sobre la finalidad de las funciones

La finalidad de las funciones , es realizar una unica accion.

Esta puede contener cualquier algoritmo y numero de instrucciones , pero con elf in de realizar una unica accion.

### 8. Inyeccion de variables

Una variable se inyecta en una cadena de texto , con el fin de que la cadena contenga variables y el valor de las variables sea contenido en la cadena.

Las variables se inyectan en las cadenas de texto mediante **modificadores** '{}'

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Cadena preparada para recibir dos datos variables: {} y {}."
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Cadena preparada para recibir dos datos variables: {dato1} y {dato2}."
```

La funcion 'format()' es un metodo del objeto string. Metodo son funciones.

Los objetos son variables

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Cadena preparada para recibir dos datos variables: {} y {}."
resultado = cadena.format(variable1, variable2)
print(resultado)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Cadena preparada para recibir dos datos variables: {dato1} y {dato2}."
resultado = cadena.format(dato1="variable1", dato2="variable2")
print(resultado)
```

### 9. Importacion de modulos

modulo. En Python un modulo es cualquier archivo o fichero .py

paquete. en python se considera paquete/package a una carpeta que contiene modulos y un archivo/fichero '__init__.py' que puede estar o no vacio

- paquete
    - "__init__.py"
    - 'modulo1.py'
    - 'modulo2.py'
    - 'modulo3.py'

Importar un modulo significa incluir el contenido de un archivo dentro de otro.

Se puede importar modulo completo o solo elementos parciales , como variables , funciones etc.

Para importar un moduo completo se utiliza la palabra clave **import** , mientras que para importar elementos se utiliza la dupla **from/import**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import modulo
import paquete.modulo
import paquete.subpaquete.modulo

from modulo import variable
from modulo import variable, funcion
from modulo import *
```

El asterisco equivale a importar todos los elementos contenidos en un modulo.
No es igual que importar todo el modulo.

import modulo  # para llamar a 'A' dentro de modulo: modulo.A
from modulo import *  # para llamar a 'A' dentro de modulo: A

#### Uso de elementos importados

Para acceder a los elementos de un modulo importado a traves del espacio de nombre importado

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import modulosypaquetes.paquete
modulosypaquetes.paquete.modulo.funcion()

import modulosypaquetes.paquete.modulo
modulosypaquetes.paquete.modulo.funcion()

from modulosypaquetes.paquete import modulo
modulo.funcion()

from modulosypaquetes.paquete.modulo import funcion
funcion()
```

#### Alias

Es posible crear alias cuando importamos , para acceder a los espacios de nombre de forma mas abreviada

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import modulosypaquetes.paquete.modulo as m
m.funcion()
```

### 10. Metodos de manipulacion de variables

Una variable es un objeto.

Se pueden realizar acciones llamadas metodos en python sobre estos objetos.

Los metodos son funciones que se desprenden de una variable, por eso la sintaxis es:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
variable.funcion()
```

En algunos casos los metodos, aceptaran parametros como cualquier otra funcion.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
variable.funcion(parametro)
```

### 11. Manipulacion de cadenas de texto

metodos que pueden aplicarse sobre una cadena de texto:

#### Metodos de Formato

##### Convertir a mayuscula la primera letra

metodo: capitalize()

retorna: copia de la cadena con primera letra en mayuscula

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion"
resultado = cadena.capitalize()
print(resultado)
```

##### Convertir una cadena a minusculas

metodo: lower()

retorna: una copia de la cadena en minusculas

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "HOla Mundo"
resultado = cadena.lower()
print(resultado)  # Salida: hola mundo
```

##### Convertir una cadena a mayusculas

metodo: upper()

retorna: una copia de la cadena en mayusculas

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "HOla Mundo"
resultado = cadena.upper()
print(resultado)  # Salida: HOLA MUNDO
```

##### Convertir Mayusculas a minusculas y viceversa

metodo: swapcase()

retorna: una copia de la cadena convertidas las mayusculas en minusculas y viceversa

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Hola Mundo"
resultado = cadena.swapcase()
print(resultado)  # Salida: hOLA mUNDO
```

##### Convertir una cadena en formato titulo

metodo: title()

retorna: una copia de la cadena convertida

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "hola mundo"
resultado = cadena.title()
print(resultado)  # Salida: Hola Mundo
```

##### Centrar un texto

metodo: center(longitud[, "caracter de relleno"])

retorna: una copia de la cadena centrada

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a la aplicacion".capitalize()
resultado1 = cadena.center(50, "=")
resultado2 = cadena.center(50, " ")
print(resultado1)  # Salida: =====Bienvenido a mi aplicacion=====
print(resultado2)  # Salida:      Bienvenido a mi aplicacion     
```

##### Alinear texto a la izquierda

metodo: ljust(longtud[, "caracter de relleno"])

retorna: una copia de la cadena alineada a la izquierda

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a la aplicacion".capitalize()
resultado1 = cadena.ljust(50, "=")
print(resultado1)  # Salida: Bienvenido a mi aplicacion==========
  
```

##### Alinear texto a la derecha

metodo: rjust(longtud[, "caracter de relleno"])

retorna: una copia de la cadena alineada a la derecha

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a la aplicacion".capitalize()
resultado1 = cadena.rjust(50, "=")
resultado2 = cadena.rjust(50, " ")
print(resultado1)  # Salida: ==========Bienvenido a mi aplicacion
print(resultado2)  # Salida:           Bienvenido a mi aplicacion
```

##### Rellenar un texto anteponiendo ceros

metodo: zfill(longitud)

retorna: una copia de la cadena rellena con ceros a la izquierda hasta alcanzar la longitud final indicada

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
numero_factura = 1575
resultado = str(numero_factura).zfill(12)
print(resultado)
```

#### Metodos de Busqueda

##### Contar cantidad de apariciones de un fragmento de texto

metodo: count("subcadena"[,posicion_inicio, posicion_fin])

retorna: un entero representando la cantidad de apariciones de subcadena dentro de cadena

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.count("a")
print(resultado)  # Salida: 3
```

##### Buscar un fragmento de texto dentro de una cadena

metodo: find("subcadena"[, posicion_inicio, posicion_fin])

retorna: un entero representando la posicon donde inicia la subcadena dentro de cadena.

Si no la encuentra retorna -1

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.find("mi")
print(resultado)  # Salida: 13 , por que la posicion 13 dentro de la cadena es donde esta 'mi'
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.find("mi", 0, 10)
print(resultado)  # Salida: -1 , por que entre la posicion 0 y 10 dentro de la cadena NO se encuentra 'mi'
```

#### Metodos de Validacion

##### Saber si una cadena comienza con un fragmento de texto determinada

metodo: startswith("subcadena"[, posicion_inicio, posicion_fin])

retorna: true o false

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.startswith("Bienvenido")
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.startswith("aplicacion")
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.startswith("aplicacion", 16)
print(resultado)  # Salida: True
```

##### Saber si una cadena finaliza con un fragmento de texto determinada

metodo: endswith("subcadena"[, posicion_inicio, posicion_fin])

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.endswith("aplicacion")
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.endswith("Bienvenido")
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "bienvenido a mi aplicacion".capitalize()
resultado = cadena.endswith("Bienvenido", 0, 10)
print(resultado)  # Salida: True
```

##### Saber si una cadena es alfanumerica

metodo: isalnum()

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo 75"
resultado = cadena.isalnum()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo"
resultado = cadena.isalnum()
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo75"
resultado = cadena.isalnum()
print(resultado)  # Salida: True
```

##### Saber si una cadena es alfabetica

metodo: isalpha()

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo 75"
resultado = cadena.isalpha()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo"
resultado = cadena.isalpha()
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo75"
resultado = cadena.isalpha()
print(resultado)  # Salida: False
```

##### Saber si una cadena es numerica

metodo: isdigit()

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo 75"
resultado = cadena.isdigit()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "7584"
resultado = cadena.isdigit()
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "75 84"
resultado = cadena.isdigit()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "75.84"
resultado = cadena.isdigit()
print(resultado)  # Salida: False
```

##### Saber si una cadena contiene solo minusculas

metodo: islower()

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepe grillo"
resultado = cadena.islower()
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Pepe Grillo"
resultado = cadena.islower()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Pepegrillo"
resultado = cadena.islower()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepegrillo75"
resultado = cadena.islower()
print(resultado)  # Salida: True
```

##### Saber si una cadena contiene solo mayusculas

metodo: isupper()

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "PEPE GRILLO"
resultado = cadena.isupper()
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Pepe Grillo"
resultado = cadena.isupper()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Pepegrillo"
resultado = cadena.isupper()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "PEPEGRILLO"
resultado = cadena.isupper()
print(resultado)  # Salida: True
```

##### Saber si una cadena contiene solo espacios en blanco

metodo: isspace()

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "pepe grillo"
resultado = cadena.isspace()
print(resultado)  # Salida: False
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "           "
resultado = cadena.isspace()
print(resultado)  # Salida: True
```

##### Saber si una cadena tiene formato tipo titulo

metodo: istitle()

retorna: True o False

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Pepe Grillo"
resultado = cadena.istitle()
print(resultado)  # Salida: True
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cadena = "Pepe grillo"
resultado = cadena.istitle()
print(resultado)  # Salida: False
```

#### Metodos de Sustitucion

##### x

##### x

##### x

##### x

##### x

#### Metodos de union y division

##### Unir una cadena de forma iterativa

##### Partir una cadena en tres partes, utilizando un separador

##### Partir una cadena en varias partes, utilizando un separador

##### Partir una cadena en lineas