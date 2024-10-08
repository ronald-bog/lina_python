from functools import reduce

''' map '''

numeros = [1, 2, 3, 4, 5]

"""  def multiplicar(x):
    return x * 2
 """
# resultado = list(map(multiplicar, numeros))

resultado = list(map(lambda x: x * 2, numeros))

print(resultado)

nombres = ['Lina','Monica','Patricia','Sofia','Juliana']
mayusculas = list(map(lambda nom: nom.upper(), nombres))
print(mayusculas)


''' filter '''

numbers = [ 54, 30, 500, 456, 83, 87, 101, 50, 22, 93 ]

resultado = list(filter(lambda item: item % 2 == 0, numbers ))
print(resultado)


''' Reduce '''

sumarNumeros = [6,7,8,9,10]

resultadoA = reduce(lambda x, y: x + y, sumarNumeros)
print(resultadoA)


