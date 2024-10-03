matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]


''' Acceso '''

#print(matriz[0][1])

''' Recorrer lista multidimensional '''

for fila in matriz:
    for elem in fila:
        print(elem, end=' ')
    print()
    

''' Crear lista multi dinamicamente '''

""" filas = 3
columnas = 3
matrizD = [[ 0 for j in range(columnas)]  for i in range(filas)]
print(matrizD) """


import random

filas = 3
columnas = 3
matrizR = [[random.randint(1,30) for j in range(columnas)]  for i in range(filas)]
print(matrizR)