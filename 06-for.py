''' FOR '''

# Sintaxis
''' 
for variable in collecion: o secuencia sobre la cual estoy iterando
    Bloque de codigo a ejecutar
'''

'''palabra = 'Margarita'
for letra in palabra:
    print(letra)'''

''' for con range '''

# for i in range(5):
# print(i)

''' Range '''
# hasta 3 args
# start
# stop
# step

# for j in range(2, 10, 2):
# print(j)

''' CONTROL DE FLUJO EN BUCLES '''

# BREAK

while True:
    respuesta = input('Escriba salir para terminar: ')
    if respuesta == 'salir':
        break

for i in range(10):
    if i == 5:
        break
    print(i)

# CONTINUE

for i in range(10):
    if i == 5:
        continue
    print(i)

i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    print(i)
    i += 1

# ELSE

for k in range(5):
    print(k)
else:
    print('El bucle finalizo')


''' ENUMERATE '''
''' sintaxis:
for indice, elemento in enumerate(iterable) :
      bloque del for
'''

frase = 'Buenas noches'
for index, elem in enumerate(frase):
    print(f'Indice: {index} - letra:{elem}')

''' ZIP '''
palabra1 = 'Python5'
palabra2 = 'VBasic'

for p1, p2 in zip(palabra1, palabra2):
    print(f'{p1} - {p2}')

for p1, p2 in zip(enumerate(palabra1), enumerate(palabra2)):
    print(f'elemento 1: {p1[1]} / indice: {p1[0]
                                           } - elemento 1: {p2[1]} / indice: {p2[0]}')

''' REVERSED '''

for num in reversed(range(7)):
    print(num)


''' SORTED ''' 

[1,2,3]

['1','2','3']

cadena = 'xhtadl'
cadena2 = '543'

for letra in sorted(cadena2):
    print(letra)
