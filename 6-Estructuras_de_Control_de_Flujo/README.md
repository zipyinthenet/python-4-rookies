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