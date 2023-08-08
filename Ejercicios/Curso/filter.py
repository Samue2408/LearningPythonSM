#Funciones de orden superior (programacion funcional)
#Verificar que los elementos de una lista cumplan una determinada condicion
#Devolviendo un objeto iterable (iterador) con los elementos que cumpliero esa condicion


edades = [12, 11, 24, 36, 8, 6, 10, 41, 32, 58, 14, 50, 7]


MayoriaEdad = lambda edad : edad >= 18

# print(filter(MayoriaEdad, edades))

edadesMayoresEdad = list(filter(MayoriaEdad, edades)) # el list lista objetos iterables
print(edadesMayoresEdad)

class Persona:

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return "{0} tiene {1} años".format(self.nombre, self.edad)
 

personas = [
     Persona("Samuel", 19),
     Persona("Angie", 21),
     Persona("Santiago", 15),
     Persona("Isabell", 6),
     Persona("Leydis", 22),
     Persona("Lucia", 11)
]

personasMayores = list(filter(lambda per: per.edad >= 18, personas))

for per in personasMayores:
    print(per)