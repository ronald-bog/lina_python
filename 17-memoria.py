import copy

variable1 = 100
variable2 = variable1
""" 
print(f'variable1 => {variable1}')
print(f'variable2 => {variable2}') """

variable1 = 50
""" print()
print(f'variable1 => {variable1}')
print(f'variable2 => {variable2}') """

variable2 = 60
""" print()
print(f'variable1 => {variable1}')
print(f'variable2 => {variable2}') """

# Mutables

lista1 = ['Lina', 'Ana', 'Jorge']
lista2 = lista1
""" print()
print(f'lista1 => {lista1}')
print(f'lista2 => {lista2}') """

lista1.append('sofia')
""" print()
print(f'lista1 => {lista1}')
print(f'lista2 => {lista2}') """

lista2.append('Peter')
""" print()
print(f'lista1 => {lista1}')
print(f'lista2 => {lista2}') """

lista2 = lista1.copy()
""" print()
print(f'lista1 => {lista1}')
print(f'lista2 => {lista2}') """

lista1.append('A')
""" print()
print(f'lista1 => {lista1}')
print(f'lista2 => {lista2}') """
lista2.append('BB')
""" print()
print(f'lista1 => {lista1}')
print(f'lista2 => {lista2}') """

personas = [
    {'nombre': 'Carlos',
     'edad': 20
     },
    {'nombre': 'Jhon',
     'edad': 25
     },
    {'nombre': 'Megan',
     'edad': 27
     }
]

# personas2 = copy.deepcopy(personas)

personas2 = [dict(persona) for persona in personas]

personas[1]['edad'] = 18
print()
print(f'personas => {personas}')
print(f'personas2 => {personas2}')

for persona in personas:
    if persona['nombre'] == 'Jhon':
        persona['edad'] = 10

print()
print(f'personas => {personas}')
print(f'personas2 => {personas2}')
