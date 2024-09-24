''' STRINGS '''

# INDICES
marcaVehiculo = 'Mazda 2'
print(marcaVehiculo[1:3])
# len() longitud del string

texto = '   python es dinamico   '
print(texto.upper())
print(texto.lower())
print(texto.strip())
print(texto.replace("dinamico", "multiparadigma"))
print(texto.count("i"))

''' f-strings '''
nombre = 'Lina'
print(f'Hola {nombre}')

''' INPUT '''

entrada = int(input('Dame un numero: '))

print(type(entrada))
