''' iteracion de diccionarios '''
valor = 12000

supermercado = {
    'Arroz': 3000,
    'leche': 4000,
    'papa': 1200,
    'pan': 5000,
    'jamon': valor
}

# Claves

# for producto in supermercado:
# print(producto)

# Valores

# for precio in supermercado.values():
#    print(precio)

# pareja K - V

# for producto, valor in supermercado.items():
#    print(f' {producto} -> {valor}')


''' Comprension de diccionarios '''

colores = ['Azul', 'Rojo', 'Verde', 'Amarillo', 'Blanco', 'Negro']

codigos = {f'C{key + 1}': values for key, values in enumerate(colores)}

# print(codigos)

valores = list(codigos.values())
# print(valores)

''' Fusion de Diccionarios '''

teclado = {'tipo': 'mecanico', 'idioma': 'ingles', 'board': 'Gigabyte'}

torre = {'procesador': 'intel', 'ram': '128GB',
         'disco': 'Samsung NVME', 'board': 'Asus'}

pc = torre | teclado
# print(pc)


''' Ordenacion'''

# por Claves

resultados = {
    'Claudia': 3.5,
    'Tomas': 4.5,
    'Roger': 4.8,
    'Lina': 5.0,
    'Carlos': 2.5
}

resultadosPorNombre = dict(sorted(resultados.items()))
# print(resultadosPorNombre)

# por valores

resultadosPorNota = dict(sorted(resultados.items(), key=lambda elem: elem[1]))

print(resultadosPorNota)

''' Diccionarios en fuunciones '''

lenguaje = {
    'nombre': 'Python',
    'framework': 'flask',
    'anio': '1989',
    'creador': 'Guido Van Rossun'
}


def revisar(nombre, framework, anio, creador):
    print(nombre)
    print(framework)
    print(anio)
    print(creador)


revisar(**lenguaje)

# * En parametros

carroA = {
    'marca': 'Renault',
    'anio': 2024,
    'motor': 1600
}


def carro(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} => {valor}')


carro(marca='Renault', anio=2024, motor=1600)

print('******************************')


def caracteristicas(diccionario):
    for key, value in diccionario.items():
        print(f'{key} = {value}')


caracteristicas(carroA)
