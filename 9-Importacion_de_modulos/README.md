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