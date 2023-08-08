# Generadores: Permiten extraer valores de una funcion y almacenarlos
# ( de uno a uno ) en objetos iterables que se pueden recorrer
# sin la necesidad de almacenar todos a la vez en la memoria ram

"""
Esto es cargando la memoria ram
def generaMultiplos7(limite):
    numero = 1
    ListaNumero = []

    while numero <= limite:
        ListaNumero.append(numero*7)
        numero += 1
    
    return ListaNumero

print(generaMultiplos7(10))

"""


def generadorMultiplos7(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7  # Ceder. "yield" genera un objeto iterable
        numero += 1


obtineMultiplo7 = generadorMultiplos7(10)

# print(obtineMultiplo7)
for n in obtineMultiplo7:
    print(n)

# next(): Retorna el siguiente elemento de un objeto iterable

print(next(obtineMultiplo7))
print(next(obtineMultiplo7))
print(next(obtineMultiplo7))

# Son mas eficientes que las funciones tradicionales
# Muy utiles con listas de valores infinitos
