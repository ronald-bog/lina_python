''' DICCIONARIOS '''

vacio = {}
lleno = {
    'nombre': 'Jhon',
    'edad': 50,
}

# * Acceso con corchetes
# print(lleno['nombre'])

# * Acceso con .get()
# print(lleno.get(1))

# * Crear diccionario con dict() - Constructor

elDiccionario = dict(nombre='Juan', edad=50)

# print(elDiccionario)

# * Modificar diccionario

lenguaje = {
    'nombre': 'Python',
    'framework': 'flask',
    'anio': '1989'
}

clave = 'framework'

lenguaje[clave] = 'Django'

# print(lenguaje)

# * Agregar par K V

lenguaje['tipado'] = 'Dinamico'

# print(lenguaje)

lenguaje['tipado'] = 'estatico'

# print(lenguaje)

# * METODOS diccionarios

lenguaje = {
    'nombre': 'Python',
    'framework': 'flask',
    'anio': '1989',
    'creador': 'Guido Van Rossun'
}

#! del: Eliminar un elemento especifico

# del lenguaje['anio']
# print(lenguaje)

#! pop()
valor = lenguaje.pop('framework')
# print(valor)
# print(lenguaje)

#! popitem()

eliminado = lenguaje.popitem()
# print(eliminado)
# print(lenguaje)

#! clear()
# lenguaje.clear()
# print(lenguaje)

lenguaje = {
    'nombre': 'Python',
    'framework': 'flask',
    'anio': '1989',
    'creador': 'Guido Van Rossun',
    1: None,
    # (x , y): (1,5)
}
#! keys()
claves = lenguaje.keys()
# print(list(claves))

#! values()
valores = lenguaje.values()
# print(list(valores))

#! items()
elementos = lenguaje.items()
# print(list(elementos))

#! update()
dicc = {'build': 'interpretado', 'version': '3.12'}

lenguaje.update(dicc)
# print(lenguaje)

#! setdefault

teclado = {'tipo': 'mecanico', 'idioma': 'Español'}
# marca = teclado.setdefault('marca', 'Redragon')
# print(teclado)
# print(marca)

tipo = teclado.setdefault('tipo', 'membrana')
# print(teclado)
# print(tipo)

#! fromkeys
keys = ['procesador', 'memoria', 'disco', 'board']

computador = dict.fromkeys(keys, None)
#print(computador)

computador['memoria'] = '32 GB'
#print(computador)

#! copy
copyComputador = computador.copy()
print(computador)
print(copyComputador)

