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

# Argumentos nombrados


def argNom(nombre, a='Hola'):
    mensaje = f'{a} {nombre}, un gusto!!!'
    return mensaje


print(argNom(a='Como estas', nombre='Maria'))

# Anotaciones de tipo 

def multiplicar(a: int, b: int) -> int:
    return a + b

def multiplicar(a, b):
    return a + b

# Parametros Variables

def sumar(**kwargs):
    return sum(args)

print(sumar(5, 10, 15, 30, 100))


''' Funciones lambda '''

sumaL = lambda a, b: a + b
#print(sumaL(10, 30))

verifPar = lambda num: 'Es par' if num%2==0 else 'Es impar'
print(verifPar(10))

sumarArgs = lambda *args: sum(args)
print(sumarArgs(200,300,500,1000,3000))
