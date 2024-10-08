from functools import reduce

sumarNumeros = [6,7,8,9,10]

resultadoA = reduce(lambda x, y: x + y, sumarNumeros)
print(resultadoA)