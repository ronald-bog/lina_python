''' TUPLAS '''

''' ACCESO ELEMTNOS '''

tupla = ('d', 'f', 'g')
# print(tupla[1])

''' tupla de un solo elemento '''

tuplaUno = (56,)
# print(type(tuplaUno))

''' tupla implicita '''

tuplaImplicita = 'React', 'Django', 'Angular'
# print(type(tuplaImplicita))


''' Desempaquetamiento '''

r, d, a = tuplaImplicita
print(r)
print(d)
print(a)


''' inmutabilidad '''

scores = (4.2, 3.5, 2.4)
scores[1] = 3.0
# print(scores)

#! Si la tupla contiene elementos mutables, ESTOS SI SE PUEDEN MUTAR

tuplaConMutables = (500, 21, [6, 8], 102)
tuplaConMutables[2][1] = 10

print(tuplaConMutables)


''' Metodos para las tuplas '''

# count()

tuplita = (1, 2, 3, 4, 4, 5)
print(tuplita.count(4))

# index()
tuplaI = 1, 2, 3, 4, 4, 5
print(tuplaI.index(3))
