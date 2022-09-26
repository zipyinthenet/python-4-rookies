#!/usr/bin/env python3
#En python una variable es un espacio para almacenar datos modificables
#En python una variable se define con la siguiente sintaxis
# nombre_de_la_variable = valor_de_la_variable

mi_primera_variable_con_valor = 20

print(mi_primera_variable_con_valor)

# ----------------------------------------------------------------------
# Tipos de datos en las variables

# cadena de texto string

mi_cadena = "Hola mundo!"
otra_cadena_mas = 'Hola chavales y chavalas!'

mi_cadena_multilinea = """
Esto es una cadena
multilinea para tener varias lineas
"""

print(mi_cadena,otra_cadena_mas,mi_cadena_multilinea)

# Numeros enteros

edad = 27
print(edad)

# Numero real

precio = 35.05
print(precio)

# Booleano verdadero o falso

verdadero = True

falso = False

print(verdadero,falso)

# ----------------------------------------------------------------------
# Tipos de datos complejos en las variables

# Tuplas
# variable que permite almacenar varios datos inmutables (parecido constantes)
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
print(mi_tupla[1:2])

# Listas
# variable que permite almacenar varios datos que si pueden ser modificados (parecido a las variables)
mi_lista = ['cadena de texto dos', 20, 3.8, 'otro dato mas', 30]
mi_lista[1] = mi_lista[1] - 5
print(mi_lista[1])

# Diccionarios
# los valores de un diccionario se asocian a un nombre clave
mi_diccionario = {
    'clave_1': 'valor_1',
    'clave_2': 'valor_2',
    'clave_3': 'valor_3',
    'clave_7': 'valor_7'
}
print(mi_diccionario['clave_2'])

# borrar entrada Diccionario
del(mi_diccionario['clave_2'])
print(mi_diccionario)
# modificar el valor
mi_diccionario['valor_1'] = 'nuevo_valor_de_valor_1'
print(mi_diccionario)
# añadir nuevos elementos
mi_diccionario['nueva_clave'] = 'nuevo_elemento'
print(mi_diccionario)
