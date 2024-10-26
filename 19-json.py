# JSON
'''
Delimitado []  {}
Las claves solo pueden tener Strings y solo deb ir entre ""

Valores que pueden contener:
numeros
Strings
Bool
null (None)
Objetos
Arrays
float
'''

''' JSON en python
A partir diccionario
- Claves tuplas no validas
- Claves enteros, se convierten a strings
- valores True, se convierten true
- valores None, se convierten null
- valor tupla, se convierten array
- valor set, no permitido

'''


import json
archivo = {
    "nombre": "Lina",
    50: None,
    "diccionario": {
        "valor": 1
    }
}

jsonConvert = json.dumps(archivo)
print(jsonConvert)

recibido = '{"nombre": "Lina", "50": null, "diccionario": {"valor": 1}}'

diccionarioConvertido = json.loads(recibido)
print(diccionarioConvertido)
print(type(diccionarioConvertido))