# * Bloques
'''
try:
    # codigo que podria presentar una excepcion
except:
    # codigo que quiero que se ejecute si se presenta una excepcion
else:
    # codigo si no se genera una excepcion try
finally:
    # se ejecuta SIEMPRE
'''

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

""" try:
    print(5/0)
    print(estudiante['nombres'])
except (KeyError, ZeroDivisionError) as e:
    if isinstance(e, KeyError):
        print(f'Clave {e} no existe')
    elif isinstance(e, ZeroDivisionError):
        print('No se puede dividir en 0') """

try:
    print(5/1)
    print(estudiante['nombres'])
except Exception as e:
    if isinstance(e, KeyError):
        print(f'Clave {e} no existe')
        print(type(e).__name__)
    elif isinstance(e, ZeroDivisionError):
        print('No se puede dividir en 0')



'''
Exception:	Clase base para todas las excepciones.
ValueError:	Valor no adecuado en una operación.
TypeError:	Operación o función con tipo incorrecto.
ZeroDivisionError:	División entre cero.
IndexError:	Índice fuera del rango de la lista.
KeyError:	Clave no encontrada en un diccionario.
AttributeError:	Atributo no encontrado en un objeto.
FileNotFoundError:	Archivo no encontrado.
IOError:	Error de entrada/salida.
ImportError:	Error al importar un módulo.
NameError:	Variable no definida.
SyntaxError:	Error en la sintaxis del código.
IndentationError:	Error de indentación en el código.
RuntimeError:	Error durante la ejecución del programa.
'''