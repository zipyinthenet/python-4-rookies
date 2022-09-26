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