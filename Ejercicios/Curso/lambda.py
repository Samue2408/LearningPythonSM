
#Son funciones anónimas que sirven para abreviar o resumir una funcion normal
#para convertirla en una expresion mas simple

# La idea del lamda es para funciones que retornan algo unico sin un proceso extenso
# Toda funcion Lambda se puedde convertir a una funcion normal pero no toda funcion se puede convertir en una funcion Lambda

"""
def sumar( n1, n2):
    return n1 + n2

print (sumar(12, 15))

"""

sumar = lambda n1, n2 : n1 + n2
print(sumar(45, 14))


elevarCuadrado = lambda numero: numero ** 2
print(elevarCuadrado(5))
