''' Funciones Void sin Params '''


def miFuncion():
    print(5+5)


miFuncion()


''' Funcion Void con Params '''

palabrasReservadas = ['for', 'if', 'def', 'in']


def agregarElemento(elemento):
    palabrasReservadas.append(elemento)


agregarElemento('while')

print(palabrasReservadas)


respuesta = miFuncion()
print(respuesta)

''' Funciones Retorno sin Params '''


def suma():
    num1 = 10
    num2 = 6
    return num1 + num2


respuestaSuma = suma()
print(respuestaSuma)


''' Funciones Retorno con Params '''
var1 = 10
var2 = 100

# Posicional


def sumar(a, b):
    r1 = var1 + a
    r2 = var2 + b
    return r1 + r2


resultadoSumar = sumar(5, 50)
print(resultadoSumar)
print(sumar(5, 50))

# Por Defecto


def paramDefault(nombre, a='Hola'):
    mensaje = f'{a} {nombre}, un gusto!!!'
    return mensaje


print(paramDefault('Lina', 'Como estas'))
