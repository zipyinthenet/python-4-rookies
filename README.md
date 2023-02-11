# CURSO python3
## Python 4 rookies

### INDICE
### [1. Primer acercamiento al Scripting](https://github.com/zipyinthenet/python-4-rookies#1-primer-acercamiento-al-scripting-1)

### [2. Acerca de Python](https://github.com/zipyinthenet/python-4-rookies#2-acerca-de-python-1)

### [3. Elementos del Lenguaje](https://github.com/zipyinthenet/python-4-rookies#3-elementos-del-lenguaje-1)

### [4. Codificacion de caracteres](https://github.com/zipyinthenet/python-4-rookies#4-codificacion-de-caracteres-1)

### [5. Tipos de datos complejos](https://github.com/zipyinthenet/python-4-rookies#5-tipos-de-datos-complejos-1)

### [6. Estructuras de Control de Flujo](https://github.com/zipyinthenet/python-4-rookies#6-estructuras-de-control-de-flujo-1)

### [7. Funciones](https://github.com/zipyinthenet/python-4-rookies#7-funciones-1)

### [8. Inyeccion de variables](https://github.com/zipyinthenet/python-4-rookies#8-inyeccion-de-variables-1)

### [9. Importacion de modulos](https://github.com/zipyinthenet/python-4-rookies#9-importacion-de-modulos-1)

### [10. Metodos de manipulacion de variables](https://github.com/zipyinthenet/python-4-rookies#10-metodos-de-manipulacion-de-variables-1)

### [11. Manipulacion de cadenas de texto](https://github.com/zipyinthenet/python-4-rookies#11-manipulacion-de-cadenas-de-texto-1)

### [12. Manipulacion de listas y tuplas](https://github.com/zipyinthenet/python-4-rookies#12-manipulaci%C3%B3n-de-listas-y-tuplas)

### [13. Manipulacion de diccionarios](https://github.com/zipyinthenet/python-4-rookies#13-manipulaci%C3%B3n-de-diccionarios)

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

##### Dar formato a una cadena , sustituyendo texto dinamicamente

metodo: format(*args, **kwargs)

retorna: la cadena formateada

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "bienvenido a mi aplicación {0}"
>>> cadena.format("en Python")
bienvenido a mi aplicación en Python
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
>>> cadena.format(100, 21, 121)
Importe bruto: $100 + IVA: $21 = Importe neto: 121
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
>>> cadena.format(bruto=100, iva=21, neto=121)
Importe bruto: $100 + IVA: $21 = Importe neto: 121
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
>>> cadena.format(bruto=100, iva=21, neto=121)
Importe bruto: $100 + IVA: $21 = Importe neto: 121
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
>>> cadena.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100)
Importe bruto: $100 + IVA: $21 = Importe neto: 121
```

##### Reemplazar texto en una cadena

metodo: replace("busqueda", "reemplazo")

retorna: la cadena reemplazada

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> buscada = "nombre apellido"
>>> reemplazo = "Juan Pérez"
>>> "Estimado Sr. nombre apellido:".replace(buscada, reemplazo)
Estimado Sr. Juan Pérez:
```

##### Eliminar caracteres a la izquierda y derecha de una cadena

metodo: strip(["caracter"])

retorna: la cadena sustituida

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = " www.ejemplo.com "
>>> cadena.strip()
www.ejemplo.com
>>> cadena.strip(' ')
www.ejemplo.com
```

##### Eliminar caracteres a la izquierda de una cadena

metodo: lstrip(["caracter"])

retorna: la cadena sustituida

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "www.ejemplo.com"
>>> cadena.lstrip("w." )
ejemplo.com
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "    www.ejemplo.com"
>>> cadena.lstrip()
www.ejemplo.com
```

##### Eliminar caracteres a la derecha de una cadena

metodo: rstrip(["caracter"])

retorna: la cadena sustituida

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> cadena = "www.ejemplo.com    "
>>> cadena.rstrip( )
www.ejemplo.com
```

#### Metodos de union y division

##### Unir una cadena de forma iterativa

metodo: join (iterable)

retorna: la cadena unida con el iterable (la cadena es separada por cada uno de los elementos del iterable)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> rellenos = ("Nº 0000-0", "-0000 (ID: ", ")")
>>> numero = "275"
>>> numero_factura = numero.join(rellenos)
>>> numero_factura
Nº 0000-0275-0000 (ID: 275)
```

##### Partir una cadena en tres partes, utilizando un separador

metodo: partition("separador")

retorna: una tupla de tres elementos dodne el primero es el contenido de la cadena previo al separador, el segundo , el separador mismo y el tercero, el contenido de la cadena posterios al separador.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> url = "https://www.ejemplo.com"
>>> tupla = url.partition("www.")
>>> tupla
('https://', 'www.', 'ejemplo.com')
>>> protocolo, separador, dominio = tupla
>>>> "Protocolo: {0}\nDominio: {1}".format(protocolo, dominio)
Protocolo: https://
Dominio: ejemplo.com
```

##### Partir una cadena en varias partes, utilizando un separador

metodo: split("separador")

retorna: una lista con todos elementos encontrados al dividir la cadena por un separador

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> keywords = "python, guia, curso".split(", ")
>>> keywords
['python', 'guia', 'curso']
```

##### Partir una cadena en lineas

metodo: splitlines()

retorna: una lista donde cada elemento es una fraccion de la cadena dividida en lineas

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> texto = """Linea 1
Linea 2
Linea 3
Linea 4
"""
>>> texto.splitlines()
['Linea 1', 'Linea 2', 'Linea 3', 'Linea 4']

>>> texto = "Linea 1\nLinea 2\nlinea 3"
>>> texto.splitlines()
['Linea 1', 'Linea 2', 'Linea 3']
```

### 12. Manipulación de listas y tuplas

En este capitulo, se veran los metodos que posee el objeto lista.
Algunos de ellos , tambien se encuentran disponibles para las tuplas.

#### Métodos de agregado

##### Agregar un elemento al final de la lista

metodo: append("nuevo elemento")

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos = ["Alvaro", "Jacinto", "Miguel", "Edgardo", "David"]
>>> nombres_masculinos.append("Jose")
>>> nombres_masculinos
['Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose']
```

##### Agregar varios elementos al final de la lista

metodo: extend(otra_lista)

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.extend(["Jose", "Gerardo"])
>>> nombres_masculinos
['Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose', 'Gerardo']
```

##### Agregar un elemento en una posición determinada

metodo: insert(posicion, "nuevo elemento")

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.insert(0, "Ricky")
>>> nombres_masculinos
['Ricky', 'Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose', 'Gerardo']
```

#### Métodos de eliminación

##### Eliminar el ultimo elemento de la lista

metodo: pop()

retorna: el elemento eliminado

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.pop()
'Gerardo'
>>> nombres_masculinos
['Ricky', 'Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose']
```

##### Eliminar un elemento por su índice

metodo: pop(indice)

retorna: el elemento eliminado

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.pop(3)
'Edgardo'

>>> nombres_masculinos
['Ricky', 'Alvaro', 'David', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose']
```

##### Eliminar un elemento por su valor

metodo: remove("valor")

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.remove("Jose")
>>> nombres_masculinos
['Ricky', 'Alvaro', 'David', 'Jacinto', 'Ricky', 'Jose', 'Jose']
```

#### Métodos de orden

##### Ordenar una lista en reversa (invertir orden)

metodo: reverse()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.reverse()
>>> nombres_masculinos
['Jose', 'Jose', 'Ricky', 'Jacinto', 'David', 'Alvaro', 'Ricky']
```

##### Ordenar una lista en forma ascendente

metodo: sort()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.sort()
>>> nombres_masculinos
['Alvaro', 'David', 'Jacinto', 'Jose', 'Jose', 'Ricky', 'Ricky']
```

##### Ordenar una lista en forma descendente

metodo: sort(reverse=True)

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.sort(reverse=True)
>>> nombres_masculinos
['Ricky', 'Ricky', 'Jose', 'Jose', 'Jacinto', 'David', 'Alvaro']
```

#### Métodos de búsqueda

##### Contar cantidad de apariciones elementos

metodo: count(elemento)

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"]
>>> nombres_masculinos.count("Miguel")
2
```

##### Obtener número de índice

metodo: index(elemento[, indice_inicio, indice_fin])

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> nombres_masculinos.index("Miguel")
1

>>> nombres_masculinos.index("Miguel", 2, 5)
4
```

#### Anexo sobre listas y tuplas

##### Conversión de tipos

se pueden convertir listas en tuplas y viceversa

metodo: list(tupla)

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> tupla = (1, 2, 3, 4)
>>> tupla
(1, 2, 3, 4)

>>> list(tupla)
[1, 2, 3, 4]
```

metodo: tuple(lista)

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> lista = [1, 2, 3, 4]
>>> lista
[1, 2, 3, 4]

>>> tuple(lista)
(1, 2, 3, 4)
```

##### Concatenación de colecciones

se pueden concatenar las listas con las listas y las tuplas con las tuplas

metodo:

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> lista1 = [1, 2, 3, 4]
>>> lista2 = [3, 4, 5, 6, 7, 8]
>>> lista3 = lista1 + lista2
>>> lista3
[1, 2, 3, 4, 3, 4, 5, 6, 7, 8]
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> tupla1 = (1, 2, 3, 4, 5)
>>> tupla2 = (4, 6, 8, 10)
>>> tupla3 = (3, 5, 7, 9)
>>> tupla4 = tupla1 + tupla2 + tupla3
>>> tupla4
(1, 2, 3, 4, 5, 4, 6, 8, 10, 3, 5, 7, 9)
```

##### Valor maximo y minimo

obtner valor maximo y minimo de listas o de tuplas

metodo: max()
metodo: min()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> max(tupla4)
10
>>> max(tupla1)
5
>>> min(tupla1)
1
>>> max(lista3)
8
>>> min(lista1)
1
```

##### Contar elementos

contar elementos de una lista o tupla

metodo: len()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> len(lista3)
10
>>> len(lista1)
4
```

### 13. Manipulación de diccionarios

#### Métodos de eliminación

##### Vaciar un diccionario

metodo: clear()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}
>>> diccionario
{"color": "violeta", "precio": 174.25, "talle": "XS"}

>>> diccionario.clear()

>>> diccionario
{}
```

#### Métodos de agregado y creación

##### Copiar un diccionario

metodo: copy()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}
>>> camiseta = diccionario.copy()
>>> diccionario
{"color": "violeta", "precio": 174.25, "talle": "XS"}

>>> camiseta
{"color": "violeta", "precio": 174.25, "talle": "XS"}

>>> diccionario.clear()
>>> diccionario
{}

>>> camiseta
{"color": "violeta", "precio": 174.25, "talle": "XS"}

>>> musculosa = camiseta
>>> camiseta
{"color": "violeta", "precio": 174.25, "talle": "XS"}

>>> musculosa
{"color": "violeta", "precio": 174.25, "talle": "XS"}

>>> camiseta.clear()
>>> camiseta
{}

>>> musculosa
{}
```

##### Crear un nuevo diccionario desde las claves de una secuencia

metodo: dict.fromkeys(secuencia[, valor por defecto])

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> secuencia = ["color", "talle", "marca"]
>>> diccionario1 = dict.fromkeys(secuencia)
>>> diccionario1
{'color': None, 'marca': None, 'talle': None}

>>> diccionario2 = dict.fromkeys(secuencia, 'valor x defecto')
>>> diccionario2
{'color': 'valor x defecto', 'marca': 'valor x defecto', 'talle': 'valor x defecto'}
```

##### Concatenar diccionarios

metodo: update(diccionario)

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> diccionario1 = {"color": "verde", "precio": 45}
>>> diccionario2 = {"talle": "M", "marca": "Lacoste"}
>>> diccionario1.update(diccionario2)
>>> diccionario1
{'color': 'verde', 'precio': 45, 'marca': 'Lacoste', 'talle': 'M'}
```

##### Establecer una clave y valor por defecto

metodo: setdefault("clave"[, None|valor_por_defecto])

Si la clave no existe , la crea con el valor por defecto.
Siempre retorna el valor para la clave pasada como parámetro.

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> camiseta = {"color": "rosa", "marca": "Zara"}
>>> clave = camiseta.setdefault("talle", "U")
>>> clave
'U'

>>> camiseta
{'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

>>> camiseta2 = camiseta.copy()
>>> camiseta2
{'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

>>> clave = camiseta2.setdefault("estampado")
>>> clave
>>> camiseta2
{'color': 'rosa', 'estampado': None, 'marca': 'Zara', 'talle': 'U'}

>>> clave = camiseta2.setdefault("marca", "Lacoste")
>>> clave
'Zara'

>>> camiseta2
{'color': 'rosa', 'estampado': None, 'marca': 'Zara', 'talle': 'U'}
```

#### Métodos de retorno

##### Obtener el valor de una clave

metodo: get(clave[, "valor x defecto si la clave no existe"])

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>> camiseta
{'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

>>> camiseta.get("color")
'rosa'

>>> camiseta.get("stock")
>>> camiseta.get("stock", "sin stock")
'sin stock'


```

##### Saber si una clave existe en el diccionario

metodo: 'clave' in diccionario

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>> camiseta
{'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

>>> existe = 'precio' in camiseta
>>> existe
False

>>> existe = 'color' in camiseta
>>> existe
True

```

##### Obtener las claves y valores de un diccionario

metodo: items()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

for clave, valor in diccionario.items():
    clave, valor

Salida:
('color', 'rosa')
('marca', 'Zara')
('talle', 'U')
```

En Python2 existia iteritems():

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>> a = dict(a=1, b=2)
>>> a.iteritems()
```

En Python3 ya no existe:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>> a.iteritems()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute
'iteritems'
```

Debe emplearse items() para generar código híbrido. no obstante, tener en cuenta que los objetos retornados se verán de forma diferente en ambas versiones.
Python3:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>> a.items()
dict_items([('a', 1), ('b', 9)])
```

Python2:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
>>> a.items()
[('a', 1), ('b', 9)]
```

Sin embargo, se itera igual en las dos:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for tupla in a.items():
    tupla
('a', 1)
('b', 9)    
```

##### Obtener las claves de un diccionario

metodo: keys()

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
for clave in diccionario.keys():
    clave
'marca'
'talle'
'color'    
```

Obtener claves en una lista:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

>>> diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
>>> claves = list (diccionario.keys())
>>> claves
['color', 'marca', 'talle']
```

##### Obtener los valores de un diccionario

metodo: values()

retorna: 

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
for clave in diccionario.values():
    clave

'rosa'
'Zara'
'U'
```

Obtener valores en una lista:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
claves = list(diccionario.values())
```

Salida:
['Zara', 'U', 'rosa']

##### Obtener la cantidad de elementos de un diccionario

Para contar los elemetos de un diccionario, al igual que con las listas y tuplas, se utiliza la funcion integrada len()

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
len(diccionario)
# Salida: 3

```

### 14. Manejo y manipulación de archivos

2 niveles para trabajar con ficheros y directorios

Uno de ellos es con el modulo 'os' , facilita el trabajo con el sistema de ficheros y directorios a nivel del propio S.O.

Segundo nivel , permite manipular ficheros su lectura y escritura desde la propia apliación o el script creado , tratando cada fichero como un objeto.

#### Modos de Apertura de un archivo

Existen varios modos de abrir un fichero , leer, escribir, o leer y escribir.

Cuando abres un fichero , se crea un puntero en memoria

r -> solo lectura -> ubicacion puntero: inicio fichero
rb -> solo lectura modo binario -> ubicacion puntero: inicio fichero
r+ -> lectura y escritura -> ubicacion puntero: inicio fichero
rb+ -> lectura y escritura modo binario -> ubicacion puntero: inicio fichero

w -> solo escritura, sobreescribe fichero si existe, crea el fichero si no existe -> ubicacion puntero: inicio fichero
wb -> solo escritura modo binario, sobreescribe fichero si existe, crea el fichero si no existe -> ubicacion puntero: inicio fichero
w+ -> escritura y lectura, sobreescribe fichero si existe, crea el fichero si no existe -> ubicacion puntero: inicio fichero
wb+ -> escritura y lectura modo binario, sobreescribe fichero si existe, crea el fichero si no existe -> ubicacion puntero: inicio fichero

a -> agregar contenido, crea fichero si no existe -> ubicacion puntero: si fichero existe al final del fichero, si el fichero no existe, al comienzo.
ab -> agregar contenido en modo binario, crea el fichero si no existe -> ubicacion puntero: si fichero existe al final del fichero, si el fichero no existe, al comienzo.
a+ -> agregar contenido y lectura, crea el fichero si no existe -> ubicacion puntero: si fichero existe al final del fichero, si el fichero no existe, al comienzo.
ab+ -> agregar contenido y lectura modo binario, crea el fichero si no existe -> ubicacion puntero: si fichero existe al final del fichero, si el fichero no existe, al comienzo.

#### Algunos métodos del Objeto File

El objeto file , dispone de algunos métodos , algunos de ellos son(el resto a buscar o consultar por internet):

read([bytes]) -> lee el contenido de un fichero, si le pasas cantidad de bytes, leera solo esa cantidad del fichero.

readlines() -> lee todas las líneas de un fichero

write(cadena) -> escribe cadena en el fichero

writelines(secuencia) -> secuencia será cualquier iterable cuyos elementos seran escritos uno por línea.

#### Accesos a archivos mediante la estructura with

La estructura with y la funcion open(), puede abrirse un fichero en cualquier modo y trabajar con él, sin necesidad de cerrarlo o destruir el puntero.

leer un fichero:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
```

escribir en un archivo:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
contenido = """
    Este será el contenido del nuevo archivo.
    El archivo tendrá varias líneas.
"""

with open("archivo.txt", "r") as archivo:
    archivo.write(contenido)
```

### 15. Manejo de archivos CSV

#### Algunos ejemplos archivos CSV

csv "comma separated values" (valores separados por coma) , archivos de texto plano , destinados al almacenamiento de datos.

ejemplos:

- Datos meteorologicos separados por ';'

ID;DATA;VV;DV;T;HR;PPT;RS;P
0;2016-03-01 00:00:00;;;9.9;73;;;

- Puntuaje por jugadores de un torneo separados por coma

nombre,cantidad,año
Maria,858,1930

- Datos de empresas registradas separados por ',' y datos entre '""'

"numero_correlativo","tipo_societario","detalles"
"10","10","bar de barrio"

- Datos almacenados en archivos de TXT con formato similar en un CSV

FECHA       TMAX    TMIN    NOMBRE
-----       ----    ----    ---------------
07122017    28.0    19.0    PELUQUERIAS

#### Trabajar con archivos CSV desde Python

Modulo 'csv' , facilita el parseo de los datos de archivos CSV , para lectura y escritura.

El modulo 'csv' se utiliza en combinación con la estructura 'with' y la función 'open' para leer , generar archivo.
El modulo 'csv' para su analisis(parsing).

##### Lectura de archivos CSV

contenido de archivo.csv

0;2016-03-01 00:00:00;;;9.9;73;;;

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from csv import reader

with open("archivo.csv", "r") as archivo:
    documento = reader(archivo, delimiter=';', quotechar='"')
    for fila in documento:
        ' '.join(fila)

```

salida:
'0 2016-03-01 00:00:00  9.9 73  '

cuando el fichero CSV tiene una cabecera, es necesario saltar dicho encabezado:

contenido archivo.csv

ID;DATA;VV;DV;T;HR;PPT;RS;P
0;2016-03-01 00:00:00;;;9.9;73;;;

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from csv import reader

with open("archivo.csv", "r") as archivo:
    documento = reader(archivo, delimiter=';', quotechar='"')
    cabeceras = next(documento)
    for fila in documento:
        ' '.join(fila)

```

salida:
'0 2016-03-01 00:00:00  9.9 73  '

Otra forma de leer arhivos CSV con cabeceras, es usar el objetivo 'DictReader' en vez de 'reader' y asi acceder solo al valor de las columnas deseadas, por su nombre:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from csv import DictReader

with open("archivo.csv", "r") as archivo:
    documento = DictReader(archivo, delimiter=';', quotechar='"')
    for fila in documento:
        fila['DATA']

```

salida:
'0 2016-03-01 00:00:00'

##### Escritura de archivos CSV

Escritura de un CSV sin cabecera:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from csv import writer

with open("datos.csv", "w") as archivo:
    doc = writer(archivo, delimiter=';', quotechar='"')
    doc.writerows(matriz)
```

En el ejemplo anterior, una matriz podria ser una lista de listas con igual cantidad de elementos. Por ejemplo:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
matriz = [
    ['Juan', 373, 1970],
    ['Ana', 124, 1983],
    ['Pedro', 901, 1650],
    ['Rosa', 300, 2000],
    ['Juana', 75, 1975],
]
```

Lo anterior generaria un fichero llamado datos.csv

```bash
cat datos.csv

Juan;373;1970
Ana;124;1983
Pedro;901;1650
Rosa;300;2000
Juana;75;1975
```

Escritura de un csv con cabeceras:

La matriz siguiente se compone de una lista de diccionarios donde las claves coinciden:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
matriz = [
    dict(jugador='Juan', puntos=300, año=2005)
    dict(jugador='Ana', puntos=100, año=2022)
    dict(jugador='Pedro', puntos=50, año=2021)
    dict(jugador='Rosa', puntos=70, año=2001)
    dict(jugador='Juana', puntos=80, año=1998)
]

from csv import DictWriter

cabeceras = ['jugador', 'puntos', 'año']

with open("datos.csv", "w") as archivo:
    documento = DictWriter(
        archivo, delimiter=';',
        quotechar='"',
        fieldnames=cabeceras
    )
    documento.writeheader()
    documento.writerows(matriz)
```

### 16. Manipulación avanzada de cadenas de texto

Python tiene soporte nativo para busquedas con expresiones regulares.

Expresion regular es un patron de caracteres de reconomiento.

Cuando se aplica una expresion regular a una cadena de texto , permite encontrar fragmentos de texto que coincidan con esa expresion.

Para crear patrones y definirlos se crean mediante caracteres de forma simbolica.

Ejemplo:
 '^ho' -> cadena que empieza por 'ho'
 'la$' -> cadena que finaliza por 'la'

 Lista de caracteres simbolicos para expresiones regulares:

 - Caracteres de posicion:
  '^' -> inicio de cadena
  '$' -> final de cadena

 - Cuantificadores:
  '?' -> cero o uno
  '*' -> cero o mas 
  '+' -> uno o mas
  '{n}' -> n veces
  '{n,}' -> n o mas veces
  '{,m}' -> entre 0 y n veces
  '{n,m}' -> entre n y m veces

 - Caracteres de posicion , agrupamiento:
  '(...)' -> grupo exacto
  '[...]' -> caracteres opcionales y rangos
  '|' -> operador logico <<or>> (A|B)
  '-' -> usado para expresar un rango [a-z]

 - Caracteres de formato:
  '\' -> caracter de escape para expresar literales
  '\d' -> digito
  '\D' -> caracter que no sea un digito
  '.' -> cualquier caracter excepto el salto de linea
  '\n' -> salto de linea
  '\s' -> espacio en blanco
  '\S' -> caracter que no sea espacio en blanco
  '\w' -> palabra
  '\W' -> caracter que no sea una palabra

#### Expresiones regulares en Python

El modulo 're' sirve para realizar busquedas mediante expresiones regulares.
Este modulo tiene la funcion 'search' para realizar busquedas mediante sintaxis:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
search(expresion, cadena)
```

Una busqueda mediante funcion 'search' , en caso de encontrar una coincidencia , retorna un objeto 'SRE_Match'.
Se accede a cada grupo de coincidencia con el metodo 'group(indice)'

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from re import search
cadena = "hola mundo"
ser = search("a\sm", cadena)
ser.group(0)
```
'a m'

En la administracion de sistemas Linux , el uso del constructor 'with' para abrir ficheros, combinado con metodos del 'objeto string' y 'expresiones regulares' , se puede emplear para analisis de registros del sistema.

ejemplo con '/var/log/auth.log'

Dec  3 20:07:16 serverrpi sshd[27860]: Failed password for invalid user joselito from x.x.x.x port 51072 ssh2

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from re import search

with open ("/var/log/auth.log", "r") as f:
    log = f.read()

regex = "(.)+: Failed password for invalid user [a-z]+\n"
ser = search(regex, log)
```

>>> ser.group(0)
Dec  3 20:07:16 serverrpi sshd[27860]: Failed password for invalid user joselito from x.x.x.x port 51072 ssh2

 - expresion anterior:

(.)+ -> indica cualquier caracter una o mas veces. Esto coincide con la fecha del registro, comando e ID del proceso: 'Dec  3 20:07:16 serverrpi sshd[27860]' La cadena que sigue, es un literal.

[a-z]+ -> coincide con el nombre de usuario ya que indica cualquier letra entra la a y la z, repetidas una o mas veces.

\n -> el salto de linea coincidiria con el final del registro.

Se puede usar este mismo sistema para analisis de registros de servicios , sistema , etc.. por ejemplo Apache , syslog , suricata u otros..


### 17. Creando menús de opciones

#### Creando menus de opciones basico

Para crear un menu de opciones basico en terminal:

- 1. todo el script debe estar organizado en funciones

- 2. cada funcion debe tener su documentacion para definir que hace cada funcion.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def leer_archivo():
    """Leer archivo CSV"""
    return "leer" 
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def escribir_archivo():
    """Escribir archivo CSV"""
    return "escribir"
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def _sumar_numeros(lista):
    """Sumar los numeros de una lista"""
    return "privada"
```

- 3. Despues se define una lista con el nombre de las funciones , que seran accesibles desde el menu:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
funciones = ['leer_archivo', 'escribir_archivo']
```

Para automatizar la generacion del menu , basta con:

- lista del paso3

- funcion 'locals()'

- atributo '__doc__'

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
numero = 1  # se usara luego para acceder a la funcion
menu = "elija una opcion:\n"

for funcion in funciones:
    menu += "\t{}. {}\n".format(
        numero, locals()[funcion].__doc__)
    numero += 1  # incrementa el numero en cada iteracion

print(menu)
opcion = int(input("Su opcion: "))
```

Para acceder dinamicamente a la funcion elegida por el usuario, el truco consistira en emplear la opcion elegida por el usuario , de forma que la opcion elegida sea el indice para acceder al nombre de la funcion desde la lista, y recurrir nuevamente a 'locals' para invocar la funcion.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
funcion = funciones[opcione - 1]
# se obtiene el nombre de la funcion

locals()[funcion]()
# se invoca a la funcion mediante 'locals()'
```

#### Creando menus de opciones con argparse

En el apartado anterior se muestra la forma de realizar un menu de forma simple.

En este apartado vamos a ver como analizar argumentos, pasados al script, por linea de comandos, mediante el modulo 'argparse'

##### Paso 1. importar modulo

importar la clase ArgumentParser del modulo argparse:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
```

##### Paso 2. construccion de un objeto ArgumentParser

Se construye un objeto 'ArgumentParser' para establecer los argumentos que el programa recibira.

Los parametros aceptados por el metodo constructor del objeto 'ArgumentParser' (funcion '__init__') son todos opcionales.

algunos parametros:

- prog -> el nombre del programa.

- description -> descripcion del programa que se mostrara en la ayuda.

- epilog -> texto mostrado al final de la ayuda.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser

argp = ArgumentParser(
    description='Descripcion breve del programa',
    epilog='Copyright 2022 Autor bajo licencia'
)
```

##### Paso 3. Agregado de argumentos y configuracion

Para agregar un argumento puede emplearse el metodo 'add_argument'

Existen dos tipos de argumentos para declarar:

- argumentos posicionales: todos aquellos que sean declarados con un nombre en vez de usar una bandera 

- argumentos con opciones (banderas / flags): todos aquellos que empleen el prefijo de opcion '-'

Un argumento definido como 'foo' es posicional , mientras que otro se define de la siguiente manera '-f' o '--foo' sera una opcion:

argp.add_argument('foo')  # argumento posicional
argp.add_argument('--foo')  # opcion foo
argp.add_argument('-f')  # opcion f

'add_argumento' puede recibir , un solo nombre de argumento posicional o una lista de banderas de opcion (flags)

En el siguiente ejemplo , en caso de ejecutarse sin ningun argumento , el fallo se produciria por la ausencia del argumento posicional 'directorio' , pero no por la ausencia de las opciones -f o --foo

argp.add_argument('directorio')  # solo un nombre posicional
argp.add_argument('-f', '--foo')  # una lista de banderas de opcion

###### Configuracion de argumentos

metodo 'add_argument' , ademas del nombre de argumento posicional y opcion , puede recibir de forma no obligatoria, algunos parametros que establecen la forma en la que el nombre de argumento o bandera seran tratados.

parametros opcionales:

- 'action' -> accion a realizar con el parametro -> store (almacenar valor) , append (agregarlo a una lista) -> store (valor por defecto)

- 'nargs' -> cantidad de valores admitidos

- 'default' -> valor por defecto para el argumento

- 'type' -> tipo de datos

- 'choices' -> lista de valores posibles

- 'required' -> indica si el argumento es obligatorio

- 'help' -> texto de ayuda a mostrar para el argumento

- 'metavar' -> el nombre del argumento que se empleara en la ayuda

- 'dest' -> nombre de la variable en la que sera almacenado el argumento

[argparse-HOWTO](https://docs.python.org/es/3/howto/argparse.html)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
argp.add_argument(
    'vocal',  # argumento posicional
    nargs='+',  # admite uno o mas valores
    choices=['a', 'e', 'o'],  # valores posibles
    metavar='VOCAL',  # nombre de la variable a mostrar en la ayuda
    help='Vocal abierta',  # texto a mostrar como ayuda
)
```

Siguiendo el ejemplo anterior, si el programa se ejecutara sin argumentos:

usuario@host:~$ ./ejemplo.py

daria el siguiente error:

usage: ejemplo [-h] VOCAL [VOCAl ...]
curl: ejemplo: the following arguments are required:
VOCAL

y si se ejecutase con la bandera de opcion -h:

usuario@host:~$ ./ejemplo.py -h

arrojaria la siguiente ayuda:

usage: ejemplo [-h] VOCAL [VOCAl ...]

Descripcion del programa

positional arguments:
  VOCAL             Vocal abierta

optional arguments:
  -h, --help     show this help message and exit

##### Paso 4. Generacion del analisis (parsing) de argumentos

argumentos = argp.parse_args()

El metodo 'parse_args' es el encargado de generar un objeto cuyas propiedades seran los argumentos recibidos por linea de comandos. A cada argumento se accedera mediante la sintaxis:

objeto_generado.nombre_del_argumento

Por ejemplo:

argumentos.foo

Ejemplo con 'argparse':

- Menu basado en el programa curl:

Intentar imprimir los valores obtenidos mediante 'argumentos.parametro'

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

descripcion_del_programa = "{}, {}".format(
    "herramienta para transferir datos desde o hacia un servidor",
    "utilizando uno de los protocolos compatibles"
)

argp = ArgumentParser(
    prog='curl',
    description=descripcion_del_programa,
)

argp.add_argument(
    '-H', '--header',  # banderas
    action='append',  # lista de valores
    nargs='+',  # admite uno o mas valores
    type=str,  # convertir los valores a string
    metavar='LINE',  # nombre de opcion a mostrar en la ayuda
    help='Cabecera adicional a incluir en la solicitud HTTP a enviar'
)

argp.add_argument(
    '-d', '--data',
    action='append',
    nargs='+',
    type=str,
    help='envia los datos especificados en una solicitud post, al servidor http'
)

argp.add_argument(
    'url',
    type=str,
    metavar='URL',
    help='URL a la cual realizar la solicitud'
)

argumentos = argp.parse_args()

```

observaciones:

Recordar que la especificacion de la codificacion de caracteres UTF-8, en python3 no es necesario ya que por defecto se interpreta, se utiliza para hacerlo compatible con python2 y frente a algunos tipos de objetos y biblitecas.

### 18. Generación de registros de sistema

En caso de que un programa o un script del sistema , guarde registro , se puede emplear modulo 'logging'

El modulo logging provee cinco niveles de registros:

- DEBUG -> 10 -> utilizado para monitorizar el funcionamiento de un programa , para depurar y obtener info.

- INFO -> 20 -> registrar eventos afirmativos , un registro detallado de tareas ejecutadas de forma satisfactoria

- WARNING -> 30 -> emitir una alerta sobre un evento determinado , informacion indicativa de un posible fallo

- ERROR -> 40 -> registrar un error , informacion cuando no logra llevarse a cabo una tarea X.

- CRITICAL -> 50 -> registrar un error que frene la ejecucion normal del programa , cuando un error fatal es capturado y el programa esta impedido.

nivel por defecto es WARNING , en caso de querer mostrarse otro nivel como INFo o DEBUG, debera modificarse el nivel de registro por defecto.

Los registros se muestran por pantalla o se graban en un fichero.

#### Principales elementos del modulo logging

Constantes: representan distintos niveles de registro. 

- constantes: INFO, DEBUG, WARNING, ERROR, CRITICAL

Clase 'basicConfig' , es usada para inicializar un registro , configurar el nivel de registro por defecto, y opcionalmente , establecer la ruta del archivo de registro y el modo de escritura.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logging import basicConfig, INFO
basicConfig(
    filename='/var/log/programa.log',
    filemode='a',
    level=INFO
)
```

los parametros compartidos en ambas ramas del lenguaje, para 'basicConfig' con los siguientes:

- filename: ruta del archivo

- filemode: modo de apertura (comunmente 'a' [append, valor por defecto] o 'w' [escritura])

- format: establece el formato en el que se generan los registros

- datefmt: formato de fecha y hora que se utilizara en los registros 

- level: nivel de registro (cualquiera de las 5 constantes)

- stream (esta opcion no sera abarcada en el curso)

Algunos de las variables admitidas como parte del valor del parametro format, son las siguientes:

[logrecord-attributes]([](https://docs.python.org/3/library/logging.html#logrecord-attributes))

    asctime         %(asctime)s
    created         %(created)f
    filename        %(filename)s
    funcName        %(funcName)s
    levelname       %(levelname)s
    levelno         %(levelno)s
    lineno          %(lineno)d
    module          %(module)s
    msecs           %(msecs)d
    message         %(message)s
    name            %(name)s
    pathname        %(pathname)s
    process         %(process)d
    processName     %(processName)s
    relativeCreated %(relativeCreated)d
    thread          %(thread)d
    threadName      %(threadName)s

Para una descripcion detallada , ver la seccion 'logRecords Attributes' en la documentacion oficial de Python. Ambas ramas conservan las mismas variables.

'[%(asctime)s] [%(levelname)s] [pid %(process)d] MYAPP myErrorLevel Alert: %(message)s'

El ejemplo anterior, producira un registro similar al siguiente:

[2018-04-20 00:34:42,803] [WARNING] [pid 12318] MYAPP myErrorLevel Alert: posible violacion de seguridad

Para establecer el formato que tendra la fecha, mediante el parametro 'datefmt' se pueden emplear las siguientes directivas:

[time.html#time.strftime](https://docs.python.org/3/library/time.html#time.strftime)

- Funciones de registro: utilizadas par amostrar o grabar los diferentes mensajes de registro:

info(), debug(), warning(), error(), critical()

A estas funciones se les debe pasar como parametro el mensaje que se deea almacenar en el registro:

funcion("mensaje a grabar")

Tambien es posible emplear variables como parte del mensaje, utilizando modificadores formato en la cadena, y pasando las variables como argumentos:

funcion("mensaje %s %i", variable_string, variable_entero)

siguiente codigo es un ejemplo y permite entender como funciona niveles de registro y mensajes, bibliotecas:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logging import basicConfig, error, info, INFO
from sys import argv

basicConfig(
    filename='ejemplo_logging.log',
    filemode='a',
    level=INFO,
    format='[%(asctime)s] [%(levelname)s] [pid %(process)d] %(message)s',
    datefmt="%d/%m/%Y %H:%M"
)

try:
    with open(argv[1], "a") as f:
        f.write(argv[2])

    info("Agregado el texto %s al archivo %s", argv[2], argv[1])
except:
    error("Se produjo un error al intentar escribir en el archivo %s", argv[1])

try:
    with open("/var/log/foo.log", "a") as f:
        f.write("Mensaje de prueba")
except (Exception) as problema:
    error(problema)                    
```

#### Obtencion de argumentos por linea de comandos con argv

'argv' , una lista del modulo system, almacena los argumentos pasados al script por linea de comandos, siendo la ruta del archivo o nombre del ejecutable, el primer elemento de la lista.

#### Captura basica de excepciones con try y except

La estructura 'try / except' permite cpaturar excepciones que de otro modo provocarian la finalizacion abrupta del script, cuando una excepcion es lanzada.

cuando una instruccion o algoritmo tiene la posibilidad de fallar (normalmente, cuando depende de valores obtenidos al vuelo), puede colarse el codigo , dentro de la estructura 'try' y utilizar 'excep' para ejecutar una accion en caso de que el intento de ejecucion de codigo del 'try' falle. Su sintaxis podria interpretarse como la siguiente:

intentar:
    ejecutar esto
si falla:
    haz esto otro

Pasado al lenguaje de Python:

try:
    # instruccion que puede fallar
except:
    # instruccion a ejecutar en caso de que el codigo del try, falle

El tipo de excepcion lanzada, tambien es posible capturarlo:

try:
    # instruccion que puede fallar
except (TipoDeExcepcion1):
    # instruccion a ejecutar en caso de que se produzca
    # una excepcion de tipo TipoDeExcepcion1
except (TipoDeExcepcion2):
    # instruccion a ejecutar en caso de que se produzca
    # una excepcion de tipo TipoDeExcepcion2

Tambien es admisible capturar mas de un tipo de excepcion de forma simultanea:

try:
    # instruccion que puede fallar
except (TipoDeExcepcion1, TipoDeExcepcion2):
    # instruccion a ejecutar en caso de que se produzca
    # una excepcion de tipo TipoDeExcepcion1 o
    # TipoDeExcepcion2

E incluso, puedo capturarse una descripcion del error, aunque no se conozca el tipo de excepcion:

try:
    # instruccion que puede fallar
except (Exception) as descripcion_del_problema:
    # instruccion a ejecutar en caso de que se produzca
    # una excepcion de tipo TipoDeExcepcion1 o
    # TipoDeExcepcion2

Los diferentes 'tipos de excepciones', pueden estudiarse en la documentacion oficial de Python2 y de Python3.
[tipos de excepciones Python2](https://docs.python.org/2/library/exceptions.html)
[tipos de excepciones Python3](https://docs.python.org/3.7/library/exceptions.html)

Para un nivel inicial se recomienda trabajar solo con except.

### 19. Módulos del sistema (os, sys y subprocess)

Los modulos 'os' y 'subprocess' permiten manejar funcionalidades del sistema operativo y procesos del sistema.
El modulo 'sys'  provee acceso a variables del interprete del lenguaje.
El modulo 'shutil' permite manejar archivos a alto nivel.
El modulo 'os' provee funciones que operan a bajo nivel.

#### El modulo OS

[doc-modulo-os](https://docs.python.org/es/3/library/os.html#)

Con este modulo permite operar a bajo nivel con funcionalidades del sistema operativo. 
Algunas funcionalidades:

|accion|comando Linux|   Metodo   |
|------|-------------|------------|
| ACCESO A FICHEROS Y DIRECTORIOS |
| obtener directorio actual     |     pwd     |  getcwd()  |
| cambiar directorio     |     cd ruta     |  chdir(path)  |
| mover directorio trabajo a raiz     |     cd     |  chroot()  |
| modificar permisos     |     chmod     |  chmod(path,permisos)  |
| cambiar propietario     |     chown     |  chown(path,permisos)  |
| crear directorio     |     mkdir     |  mkdir(path[, modo])  |
| crear directorios recursivos     |     mkdir -p     |  mkdirs(path[, modo])  |
| eliminar fichero     |     rm     |  remove(path)  |
| eliminar directorio     |     rmdir     |  rmdir(path)  |
| renombrar fichero     |     mv     |  rename(actual,nuevo)  |
| crear enlace simbolico     |     ln -s     |  symlink(origen,destino)  |
| establecer mascara creacion ficheros     |     umask     |  umask(mascara)  |
| obtener listado ficheros y directorios     |     ls -a     |  listdir(path)  |
| obtener estado fichero     |     stat     |  stat(path)  |
| evaluacion de ficheros y directorios (modulo os.path) |
| obtener ruta absoluta     |     -     |  path.abspath(path)  |
| obtener directorio base     |     -     |  path.basename(path)  |
| saber si un directorio existe     |     -     |  path.exists(path)  |
| conocer ultimo acceso a un directorio     |     -     |  path.getatime(path)  |
| conocer tamaño del directorio     |     -     |  path.getsize(path)  |
| saber si una ruta es:     |     -     |    |
| absoluta     |     -     |  path.isabs(path)  |
| un fichero     |     -     |  path.isfile(path)  |
| un directorio     |     -     |  path.isdir(path)  |
| un enlace simbolico     |     -     |  path.islink(path)  |
| un punto de montaje     |     -     |  path.ismount(path)  |
| FUNCIONALIDADES DEL S.O. |
| obtener valor variable entorno     |     $VARIABLE     |  getenv(variable)  |
| obtener datos del s.o.     |     uname -a     |  uname()  |
| obtener UID     |     id -u     |  getuid()  |
| Obtener ID del proceso     |     pgrep     |  getpid()  |
| crear variable de entorno (del sistema)     |     export $VARIABLE     |  puntenv(variable, valor)  |
| forzar la escritura del cache al disco     |     sync     |  sync()  |
| matar un proceso     |     kill     |  kill(pid, señal)  |

#### variables de entorno: os.environ

'environ' es un direccionario del modulo 'os'.
Este direccionario tiene variables de entorno , las cuales adquieren un valor dependiente del sistema donde se ejecuten.

ver variables de entorno disponibles de 'environ':

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import environ

for variable, valor in environ.items():
    variable, valor
```

#### Ejecucion simplificada de comandos del sistema

la funcion 'system' del modulo 'os' , permite ejecutar comandos del sistema sin manejar la E/S estandar o los errores.

Se lanza directamente sobre el s.o.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import system

command = "curl http://unawebdeconsulta"
system(command)
```

con la funcion 'system' , podemos redireccionar la salida de los comandos o los errores.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import system

command = "curl http://unawebdeconsulta > salida"
system(command)
```

para acceder a la salida almacenada , se puede leer como si fuera un fichero:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import system

command = "curl http://unawebdeconsulta > salida"
system(command)

with open('salida', 'r') as f:
    salida = f.read()
```

#### Ejecucion de comandos del sistema mediante 'Popen' y 'shlex.split'

A traves de la clase 'Popen' del modulo 'subprocess' , es posible ejecutar comandos directamente sobre el s.o. y manipular tanto la E/S estandard como errores.

la funcion 'split' del modulo 'shlex' puede emplearse como complemento de 'Popen' , para el parseado de cadenas de texto como lista de comandos y argumentos.

La clase 'Popen' (process open) , abre un nuevo proceso en el sistema , y permite manejar tuberias para manejar la E/S estandard y errores.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
proceso = Popen(<comando/argumentos>, stdout=PIPE, stderr=PIPE)
```

el primer argumento pasado a 'Popen' debe ser una lista. Debe contener el comando , las opciones(banderas) , y argumentos. 
Por ejemplo:

ls -ls /home/usuario/descargas

ls -> argumento

-ls -> lista opciones

/home/usuario/descargas -> argumento

total 3 elementos

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
lista = ['ls', '-ls', '/home/usuario/descargas']
proceso = Popen(lista)
```

Sin embargo , la instruccion completa podria escribirse en una cadena de texto.
Y con la funcion 'split' del modulo 'shlex' , emplearla para generar la lista necesaria para Popen:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from shlex import split
from subprocess import Popen

comando = 'ls -ls /home/usuario/descargas'
proceso = Popen(split(comando))
```

#### Capturar la salida estandar y los errores

se pueden emplear tuberias para capturar la Salida estandar y los errores:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from shlex import split
from subprocess import Popen

comando = 'ls -ls /home/usuario/descargas'
proceso = Popen(split(comando), stdout=PIPE, stderr=PIPE)
salida = proceso.stdout.read()
errores = proceso.stderr.read()

if not errores:
    accion a realizar si no hubo errores
else:
    accion a realizar si hubo errores
```

#### Emplear la salida de un comando como entrada de otro

en la linea de comandos , se puede emplear la salida de un comando para redirigir la salida a otro comando.
Con '|' pipe.
ejemplo:

```bash
ls -ls /home/user/descargas/fichero.txt | grep 'user'
```

la salida de 'ls' se utiliza como entrada del comando 'grep'

Cuando usamos 'Popen' la salida de un comando se encuentra disponible en:

'proceso_creado.stdout'

Esta salida se puede usar como valor del argumento 'stdin' , del segundo proceso creado por 'Popen'.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from shlex import split
from subprocess import Popen, PIPE

#comandos necesarios
ls_command = "ls -ls /home/user/descargas/fichero.txt"
grep_command = "grep 'user'"

# procesos
ls_process = Popen(
    split(ls_command), stdout=PIPE, stderr=PIPE)

grep_process = Popen(
    split(grep_command),
    stdin=ls_process.stdout,
    #salida del proceso anterior como entrada
    stdout=PIPE,
    stderr=PIPE
)

#ejecucion
grep_process.stdout.read()
```

#### Variables y funciones del modulo sys

[modulo-sys-documentation](https://docs.python.org/3/library/sys.html)

algunas variables del modulo 'sys':


|variable|Descripcion|
|------|-------------|
| sys.argv | retorna una lista con todos los argumentos pasados |
| sys.executable | retorna el path absoluto del path ejecutado |
| sys.path | retorna una lista con las rutas empleadas para buscar ficheros |
| sys.platform | retorna la plataforma donde se esta ejecutando el interprete |
| sys.version | retorna el numero de version de Python e informacion adicional |

La funcion 'exit()' del modulo 'sys' se emplea para finalizar un programa o script de forma abrupta.

ejemplo:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from shlex import split
from subprocess import Popen, PIPE

ls = "ls -ls /hom/noexiste"
grep = "grep 'user'"

ps_ls = Popen(split(ls), stdout=PIPE, stderr=PIPE)

if ps_ls.stderr.read():
    exit("Terminacion abrupta tras error en comando ls")

ps_grep = Popen(
    split(grep),
    stdin=ps_ls.stdout,
    stdout=PIPE,
    stderr=PIPE
)    
```

- el mensaje pasado a la funcion 'exit()' es opcional

- la funcion 'exit()' puede recibir un entero representativo del motivo de salida (el 0 es valor por defecto, indica salida normal)

- la funcion 'exit()' del modulo 'sys' tiene un proposito similar a la constante incorporada exit , sin embargo ambos elementos no responden de la misma manera

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
print sys.exit()
```


### 20. Conexiones remotas (HTTP, FTP y SSH)

Python tiene las siguientes librerias:


- libreria 'http' para realizar conexiones a los protocolos HTTP/HTTPS

- libreria 'ftplib' para realizar conexiones a los protocolos FTP

- libreria 'Paramiko' creada por Robey Pointer , para realizar conexiones al protocolo SSH

#### Conexiones remotas via HTTP y HTTPS

El modulo 'client' de la libreria 'http' nos da la posibilidad de conectar al protocolo http.

Mediante las clases 'HTTPConnection' y 'HTTPSConnection'

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http.client import HTTPConnection
http = HTTPConnection('host.com', port=80, timeout=10)
```

port y timeout son 2 parametros opcionales.

las solicitudes se realizan mediante metodo 'request' y este requiere de dos parametros posicionales.

- metodo HTTP usado (GET,POST...)

- recurso HTTP (urn nombre de recurso uniforme)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http.client import HTTPConnection
http = HTTPConnection('host.com', port=80, timeout=10)

http.request("GET", "/foor/bar")
```

se pueden añadir otros parametros:

- headers -> diccionario con campos de cabecera

- body -> cadena de texto

parametros utiles para peticiones que requieren envio de información.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http.client import HTTPConnection
http = HTTPConnection('host.com', port=80, timeout=10)

parametros = "nombre=Juan&apellido=Perez"
cabeceras = {
    "Content-Type": "application/x-www-form-urlencoded"
}
http.request(
    "POST", "/foo/bar",
    headers=cabeceras, body=parametros
)
```

La respuesta mediante el metodo 'getresponse' , retorna un objeto 'HTTPResponse' , en sus propiedades este metodo posee 'status' (codigo de respuesta HTTP), y 'reason' (descripcion de la respuesta), entre sus metodos 'read' , retorna el cuerpo de la respuesta:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
respuesta = http.getresponse()
codigo = respuesta.status
descripcion = respuesta.reason
body = respuesta.read()
```

El cierre de una conexion HTTP se realiza mediante el metodo 'close'

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
http.close()
```

ejemplo de una peticion POST a un host local:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http.client import HTTPConnection

http = HTTPConnection('juanproyecto.local', port=80, timeout=30)
parametros = "nombre=Juan&apellido=Perez"
cabeceras = {"Content-Type": "application/x-www-form-urlencoded"}
http.request("POST", "/foor/bar", headers=cabeceras, body=parametros)
respuesta = http.getresponse()
codigo = respuesta.status
descripcion = respuesta.reason
body = respuesta.read()

body
codigo
descripcion
```

#### Conexiones remotas via FTP

La biblioteca 'ftplib' permite conexiones mediante el protocolo FTP

Para crear una instancia , se dispone de las clases 'FTP' (sin cifrado) y 'FTP_TLS' (con cifrado TLS evolución SSL)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ftplib import FTP
ftp = FTP()
```

Para abrir una conexión se empleta el metodo 'connect' , admite parametros como , host y puerto

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ftplib import FTP
ftp = FTP()

ftp.connect('algunhost.com', 21)
```

Si es necesario usar el modo pasivo , se dispone del metodo 'set_pasv'

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ftplib import FTP
ftp = FTP()
ftp.connect('algunhost.com', 21)

ftp.set_pasv(True)

```

La autenticación se realiza mediante el metodo 'login' , recibe por parametros , usuario y contraseña

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ftplib import FTP
ftp = FTP()
ftp.connect('algunhost.com', 21)
ftp.set_pasv(True)

ftp.login('algunusuario', 'clave')
```

Para cerrar una conexión se puede usar el metodo 'quit' , esto cierra la conexion de ambos lados (cliente y servidor)
El metodo 'close' cierra la conexión unilateralmente.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ftplib import FTP
ftp = FTP()
ftp.connect('algunhost.com', 21)
ftp.set_pasv(True)
ftp.login('algunusuario', 'clave')

ftp.quit()
```

Otros metodos:

|Accion|Metodo|
|------|-------------|
| Directorios | |
| Lisar directorios | dir() , dir('ruta/a/listar') |
| Crear un directorio | mkd('ruta/a/algun-dir') |
| Moverse a un directorio | cwd('ruta/a/algun-dir') |
| Eliminar un directorio | rmd('ruta/a/dir-a-borrar') |
| Obtener directorio actual | pwd() |
| Archivos | |
| Recuperar un archivo remoto | retrbinary('RETR origen', open('/ruta/destino', 'w').write) |
| Enviar un archivo local | storbinary('STOR destino/remoto.txt', open('/origen/local.txt', 'r')) |
| Eliminar un archivo | delete('archivo/a/eliminar') |
| Renombrar (mover) un archivo | rename('origen', 'destino') |

#### Solicitando la contraseña con getpass

La biblioteca 'getpass' , permite solicitar mediante un input , un password , para no tener que trabajar con el password en crudo en el codigo fuente.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from getpass import getpass
clave = getpass('Ingresar clave: ')
```

La funcion 'getpass' puede usarse de forma conjunta con metodo login (de esta forma se evita escribir la clave en crudo dentro del codigo fuente).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ftplib import FTP
from getpass import getpass

ftp = FTP()
ftp.connect('algunhost.com', 21)
ftp.login('algunusuario', getpass('Clave FTP: '))
```

#### Conexiones SSH con Paramiko

La biblioteca 'paramiko' se de instalar de forma adicional (no esta en las bibliotecas de python).
Se puede instalar a traves de PyPI (gestor de paquetes de python).
En debian se puede instalar desde apt.

##### Requisitos previos

Para instalar un paquete desde PyPI , se necesita herramienta 'pip'.

```bash
apt install python-pip  # para Python2
apt install python3-pip  # para Python3
```

Las instalaciones para Python2 y Python3 , se manejan de forma independiente.
Por tanto habra que instalar 'Paramiko' en ambas versiones.

mediante root:

```bash
pip install paramiko  # para Python2
pip3 install paramiko  # para Python3
```

[paramiko](https://www.paramiko.org/installing.html)

##### Uso de Paramiko

Una conexion SSH se inicializa con la creación de un objeto 'SSHClient':

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paramiko import SSHClient, AutoAddPolicy

ssh = SSHClient()
```

La conexión como la autenticación , se realizara de forma separada , para tener un mayor control.

Para la autenticación mediante llave pública , se empleara 'set_missing_host_key_policy' , a fin de localizar las llaves y facilitar el intercambio de las mismas:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ssh.set_missing_host_key_policy(AutoAddPolicy())
```

Normalmente , el uso de este metodo no deberia ser necesario , y bastaria con emplear 'load_system_host_keys':

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ssh.load_system_host_keys()
```

Utilizar 'set_missing_host_key_policy' , evita algoritmos complejos para captura y tratamiento de errores.

La conexion al servidor , se realizara mediante el metodo 'connect' , recibe con parametros , el host o IP del server y puerto de conexión , y nombre de usuario.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ssh.connect('x.x.x.x', 22, 'usuario')
```

Cuando se requiera autenticacion por contraseña , se puede pasar como cuarto parametro el password:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ssh.connect('x.x.x.x', 22, 'usuario', 'clave')
```

La ejecucion de comandos en el server , se realiza mediante el metodo 'exec_command' , donde se le pasa una cadena de instruccion que se desea ejecutar.
Esto retorna tres objetos , de E/S estandar y errores:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
entrada, salida, error = ssh.exec_command('ls -la')
```

Se pueden leer los objetos de salida y error mediante 'read':

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
salida.read()
error.read()
```

La entrada puede ser escrita mediante write:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
entrada.write('entrada que espera el comando \n')
salida.read()
```

Para cerrar la conexion , se utiliza close:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ssh.close()
```

### 21. Bibliotecas para el manejo avanzado de archivos, en sistemas GNU/Linux

### 22. Probabilidad y Estadística con Python

### 23. Estadística descriptiva con Python

### 24. Python como CGI para aplicaciones Web

### 25. Conexiones a bases de datos con MySQL y MariaDB

### 26. Programación orientada a objetos con Python



##### template

metodo:

retorna:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x
```