''' TRUTHY Y FALSY '''

# print(bool(True))

''' Falsy '''

# print(bool(None))
# print(bool(False))
# print(bool(0))
# print(bool(''))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(set()))

print(bool(1))
print(bool(0))

print('Es Truthy' if 0 else 'Es Falsy')
'''
if 0:
    print('Es Truthy')
else:
    print('Es Falsy')

if []:
    print('Es Truthy')
else:
    print('Es Falsy')

if 55:
    print('Es Truthy')
else:
    print('Es Falsy')
'''

# numeros = [206, 56, 96413, 64]
numeros = []

if numeros:
    for i in numeros:
        print(i)
else:
    print('La lista esta vacia, no puedo realizar operaciones')
