tupla = (1, 2, 3)
print(tupla)

tupla2 = (7, "Oscar", True, 450.1, 16 + 7j, 15, "Felicidad", False)
print(tupla2)

tupla3 = (9, 3, (4, 5, 6))
print(tupla3)

print(tupla2[1])

# tupla2[1] = "Samuel" La tuplas no se pueden modificar

print(tupla2[-1]) #acceder al ultimo elemento
print(tupla2[0:4])
print(tupla2[-2] , tupla , sep="-") #el sep se utiliza para separar con el argumento indicado las variables ingresadas

a, b, c = tupla

print(a, end=" ") #el end se utiliza para que la impresion termine en un espacio y no en un salto de linea
print(b, end=" ")
print(c)

tuplaFinal = tupla + tupla3

print(tuplaFinal)
print(tuplaFinal.count(3))
print(tuplaFinal.index(3)) #para saber la primera posicion del argumento ingresado
