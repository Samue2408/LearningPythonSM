lista_enteros = [ 1, 2, 3, 4, 5 ]
print(lista_enteros)

lista_letras = [ "a", "b", "c", "d", 'a']
print(lista_letras)

lista_varios = ["Fisica", "Matematicas", 1999, True]
print(lista_varios)

#para dar los limites de lo que se quiere imprimir del vector
print(lista_enteros[1:5])
print(lista_varios[:2])
print(lista_letras[1:])

#Repetir datos de una lista
print([1,2,3] * 3)
print(['hola'] * 3)
print(lista_enteros * 2)

#saber si un dato esta dentro de la lista
print(4 in lista_enteros)
print('hola' in ['hola', 'y'])
print(5 in lista_varios)

#Saber cuantos datos hay en la lista de dato proporcionado
print(lista_letras.count("a"))

#para invertir la lista
lista_letras.reverse()
print(lista_letras)