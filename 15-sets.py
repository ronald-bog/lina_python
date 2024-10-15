''' CONJUNTOS (SETS) '''

# ? Creacion

conjunto = {'a', 'b', 'c', 'd'}
print(type(conjunto))
print(conjunto)

conjuntoA = set([5, 6, 7, 8])
print(conjuntoA)

# ? conjuntos vacios

vacio = {}
void = set()
print(type(vacio))
print(type(void))

# ? METODOS
# * add()

conjuntoC = {45, 65, 85}
conjuntoC.add(75)
print(conjuntoC)

# * remove
conjuntoC.remove(46)
print(conjuntoC)

# * discard
conjuntoC.discard(66)
print(conjuntoC)

# * pop
conjuntoD = {'Lina', 'Juan', 'Peter', 'Monica'}
resultado = conjuntoD.pop()
print(resultado)

# * union()
set1 = {'m', 'n', 'o'}
set2 = {'n', 'r', 's'}
union = set1.union(set2)
# print(union)

# * intersection
interseccion = set1.intersection(set2)
# print(interseccion)

# * difference
diferencia = set1.difference(set2)
# print(diferencia)

# * symmetric_difference
simetrico = set1.symmetric_difference(set2)
# print(simetrico)


# * issubset
frutasA = {'pera', 'manzana', 'uva'}
frutasB = {'maracuya', 'banano', 'fresa', 'pera', 'manzana', 'uva'}
# print(frutasA.issubset(frutasB))

# * issuperset
# print(frutasB.issuperset(frutasA))

# * isdisjoint
frutasC = {'melon', 'papaya'}
# print(frutasB.isdisjoint(frutasC))

# * verificar pertenencia
print('banano' in frutasB)

listaFrutasB = list(frutasB)
print(listaFrutasB)


