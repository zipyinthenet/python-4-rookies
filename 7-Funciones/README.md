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