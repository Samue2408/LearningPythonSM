# Map: Aplica una funcion a cada elemento de una lista iterable
# Devolviendo otra lista 

elevarCuadrado = lambda num : num ** 2 # pow(num, 2)

numeros = list(range(1, 11))

elevados = list(map(elevarCuadrado, numeros))

print(elevados)
