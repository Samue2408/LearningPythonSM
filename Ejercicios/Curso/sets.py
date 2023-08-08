# Sets: son colecciones desordenadas de objetos únicos

"""

canasta ={'manzana', 'platano', 'pera', 'manzana', 'naranja', 'pera'}
print(canasta)

#Tipo 1 de Sets: Sets mutables
a = set('abracadabra')# Mutables, se pueden añadir nuevos elementos
print(a)

a.add('g')
print(a)

a.add('a')
print(a)


# Tipo 2 de Sets: Set inmutables (no se pueden añadir nuevos elementos)
b = frozenset('perro')
print(b)

"""



# INTERSECCIONES
# miSet = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) <--- esto es igual a ---
#                                                                             |
miSet = {1, 2, 3, 4, 5} & {3, 4, 5, 6} # <-----------------------------------
print(miSet)


# UNION
# miSet = {1, 2, 3, 4, 5}.union({3, 4, 5, 6}) <--- esto es igual a ----------
#                                                                             |
miSet = {1, 2, 3, 4, 5} | {3, 4, 5, 6} # <---------------------------------
print(miSet)


# DIFFERENCE
# miSet = {1, 2, 3, 4, 5}.difference({3, 4, 5, 6}) <--- esto es igual a -----
#                                                                             |
miSet = {1, 2, 3, 4, 5} - {3, 4, 5, 6} # <---------------------------------
print(miSet)


# SYMMERTRIC DIFFERENCE
miSet = {1, 2, 3, 4, 5}.symmetric_difference({3, 4, 5, 6})
print(miSet)


# SABER SI EL SET CONTIENE AL OTRO SET, devuelve un boolean
miSet = {1, 2, 3, 4, 5}.issuperset({3, 4, 5, 6})
print(miSet)

# SABER SI EL OTRO SET CONTIENE AL SET, devuelve un boolean
miSet = {1, 2, 3, 4, 5}.issubset({3, 4, 5, 6})
print(miSet)