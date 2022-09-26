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