#!/usr/bin/env python3
#Entrada y salida en python3

# Para imprimir por pantalla con la palabra clave print hasta las version 2.7
# a partir de las version 3.0 se usa la funcion print()

mi_variable = 15

print(mi_variable)

# Para la entrada , se puede obtener datos solicitados al usuario.
# hasta la version 2.7 se usa la funcion raw_input()
# a partir de la version 3.0 se usa la funcion input()

# 2.7 - en caso de ejecutarse con python3 no funciona

mi_variable_dos = raw_input("Ingresa un valor: ")

print(mi_variable_dos)

# 3.0 - funciona con python2.7 

mi_variable_tres = input("Ingresa un valor: ")

print(mi_variable_tres)
