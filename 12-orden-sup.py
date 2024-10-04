''' map '''

numeros = [1, 2, 3, 4, 5]

""" def multiplicar(x):
    return x * 2
 """
# resultado = list(map(multiplicar, numeros))

resultado = list(map(lambda x: x * 2, numeros))

print(resultado)

nombres = ['Lina','Monica','Patricia','Sofia','Juliana']
mayusculas = list(map(lambda nom: nom.upper(), nombres))
print(mayusculas)


''' filter '''
