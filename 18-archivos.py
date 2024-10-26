# MANEJO DE ARCHIVOS

# file = open('prueba.txt', 'r')
# print(file)
# file.close()

''' LECTURA DE ARCHIVO '''

# read
""" with open('prueba.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido) """

""" with open('python.png', 'rb') as file:
    imagen = file.read()
    print(imagen) """

# readline

# with open('prueba.txt', 'r', encoding='utf-8') as file, open('prueba.txt', 'r') as file2:
#     linea1 = file.readline(4)
# print(linea1)
# linea2 = file.readline()
# linea3 = file.readline()

# flag = True
# while flag:
#     linea = file.readline()
#     if  linea == '':
#         flag = False
#     else:
#         print(linea)
# qty = 0
# for j in file2:
#     qty += 1

# print(qty)

# for i in range(qty):
#     linea = file.readline()
#     print(linea.strip())

# * Parametro encoding='utf-8'

# * readlines()

# with open('prueba.txt', 'r', encoding='utf-8') as archivo:
#     lineas = archivo.readlines()
#     print(lineas)


# * ESCRITURA DE ARCHIVOS

# * write

# with open('prueba.txt', 'w', encoding='utf-8') as filew:
#     filew.write('Estamos usando write\n')
#     filew.write('esta es la segunda linea')

# * writelines()

# palabras = ['En este momento\n', 'vamas a usar\n',
#             'writelines para escribir\n', 'en el archivo\n', 'Acción']

# with open('prueba.txt', 'w', encoding='utf-8') as filewl:
#     filewl.writelines(palabras)

# * APPEND

# palabras = ['\n', 'y ahora estoy agregando\n', 'lineas con append.']
with open('pruebas.txt', 'a', encoding='utf-8') as archivo:
    archivo.writelines(palabras)

# * COMBINANDO MODOS +

# * 'r+': Lectura y escritura (el archivo debe existir)
# * 'w+': Lectura y escritura (sobrescribe)
# * 'a+': Lectura y escritura (añade)

with open('pruebas.txt', 'a+', encoding='utf-8') as archivo:
    archivo.write('octava linea')
