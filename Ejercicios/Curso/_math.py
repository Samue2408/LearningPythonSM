import math

x = 1.553

print(round(x)) # para redondear
print(round(x, 1)) # redondear hasta determinado numero de decimales

print(math.ceil(x)) # Siempre va a redondear al numero entero superior
print(math.floor(x)) # Siempre va a redondear al numero entero inferior

print(math.trunc(x)) # Toma la parte entera

numeros = [1, 2, 3, 4, 5]
print(math.fsum(numeros)) # Para sumar todos los elementos de una lista iterable

math.fabs(-4) # valor absoluto
math.fmod(17,6) # Modulo
math.exp(2) # epsilon elevado al cuadrado
math.pi # numero PI

math.pow(5, 6) # Exponentes
math.sqrt(16) # Raiz cuadrada
math.hypot(1.5, 1.5) # Hallar hipotenusa
math.radians(45) # Pasar a radianes

math.sin(67) # Hallar el seno 

math.remainder(16, 2)
print(math.remainder(17, 6))
print(math.fmod(17, 6))


