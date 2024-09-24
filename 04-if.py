# nali112@hotmail.com
""" IF """

numero = 5

# if solito
if numero < 4:
    print('la condicion que pasaste es TRUE')

print('Linea despues del IF')

# if - else
edad = 10
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

# if - elif - else

edad1 = 20
if edad1 >= 18:
    print('Eres Adulto')
elif 18 > edad1 > 12:
    print('Eres adolescente')
else:
    print('Eres niño')

# if anidado

edad2 = 20
pais = "Col"

if edad2 >= 20:
    if pais == 'España':
        print('Si Puedes votar')
    else:
        print('NO Puedes votar en España')
else:
    print('No puedes votar porque eres menor de edad')

''' Expresion ternaria if - else '''

edad = 19
""" if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad') """

print('Eres mayor de edad' if edad >= 18 else 'Eres menor de edad')


if 'Mar' not in 'Margarita':
    print('si existe')
else:
    print('no existe')
