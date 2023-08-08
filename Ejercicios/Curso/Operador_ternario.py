"""
En Java es

String sexo
sexo = (10 > 2) ? "Masculino" : "Femenino"

Esto quiere decir que si la condicion es positiva la variable "sexo" toma el valor "Masculino" 
y en caso de que la condicion sea falsa la variable toma el valor "Femanino"

"""

sexos = ("Hombre", "Mujer")

posicion = True
sexo = sexos[posicion] #toma el valor "Mujer" porque el True en logica binaria es 1
print(sexo)
sexo = sexos[not posicion] #toma el valor "Hombre" porque lo contrario de True es False y en logica binaria el False es 0
print(sexo)