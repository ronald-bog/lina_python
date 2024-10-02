''' LISTAS '''

# acceso a elementos

lista = [10, 20, 30, 40]

print(lista[-2])
print(lista[1])

''' Metodos o Funciones de las listas '''

''' append(x) '''

numeros = [101, 205, 602]
numeros.append(1001)
print(numeros)

numeros[0] = 202

print(numeros)

''' extend(iterable) '''

lista = [6, 7, 8]
lista.extend([9, 10])
lista.extend('SQL')
print(lista)

''' insert(i, x) '''
miLista = [56, 45, 21]
# iLista.insert(1, 1000)
miLista.insert(1, [1000, 2000])
print(miLista)

''' remove(x) '''
enteros = [45, 56, 20, 56, 100]
enteros.remove(56)
print(enteros)


''' pop(i) '''

numbers = [5, 6, 7, 8, 9, 10]
devuelve = numbers.pop()
print(devuelve)
print(numbers)

devuelveA = numbers.pop(0)
print(devuelveA)
print(numbers)

''' index(x) '''

numbersB = [5, 6, 7, 8, 9, 10]
print(numbersB.index(10))

''' count(x) '''
numbersB = [5, 6, 7, 8, 9, 10, 8, 9, 10, 8]
print(numbersB.count())

''' sort(reverse=False) '''

numbersDesordenada = [5, 6, 7, 8, 9, 10, 8, 9, 10, 8, 1, 2]
numbersDesordenada.sort(reverse=True)
print(numbersDesordenada)

''' reverse()  '''
reverso = ['z', 'a', 'd']
reverso.reverse()
print(reverso)

''' copy() '''
listaZ = ['Lina', 'Laura', 'Liliana']
nuevaLista = listaZ.copy()
print(nuevaLista)
# Vamos a ver mas adelante almacenamiento por valor y referencia, como unir todos los elementos de una matriz

''' clear() '''
listaZ.clear()
print(listaZ)


''' Desempaquetamiento de una lista '''
lenguajes = ['Python', 'JS', 'JAVA']

Variable1, lenguaje, cosa = lenguajes

print(Variable1)
print(lenguaje)
print(cosa)


''' LISTAS POR COMPRENSION '''

''' sintaxis:
[iten a nueva_lista for item in 'iterable']
'''

resultado = [i for i in range(6)]
print(resultado)

multiplos = [i * 3 for i in range(1, 11)]
print(multiplos)

numbers = [item*5 for item in range(10)]
pares = [item*5 for item in range(10) if item % 2 == 0]
print(numbers)
print(pares)

''' Ejemplo '''

cadena = 'Hola mundo'

vocales = [letra for letra in cadena if letra in 'aeiou']
print(vocales)
