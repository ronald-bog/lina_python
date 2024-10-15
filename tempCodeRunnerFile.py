
estudiante = {
    'nombre': 'Carlos',
    'edad': 30
}

""" try:
    print(estudiante['nombre'])
except:
    print('La clave no existe')
else:
    print('Todo el codigo de TRY salio bien')
finally:
    print('Yo me ejecuto SIEMPRE') """


try:
    print(5/1)
    print(estudiante['nombres'])
except (KeyError, ZeroDivisionError) as e:
    print('no se puede dividir en 0')
    print(e)