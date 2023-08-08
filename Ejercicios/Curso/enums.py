# Enumeradores
from enum import Enum

class Color(Enum):
    rojo = '#ff0000'
    verde = '#008000'
    azul = '#0000ff'

#print(Color.rojo.value)
#print(Color('#008000'))
#print(Color['rojo'].value)
 
lista = [c for c in Color]
print(lista)
