#SAMUEL MALDONADO MONTERO

cadena = input("Introduce una palabra o frase: ")

cadena = cadena.lower().replace(" ", "")

if cadena == cadena[::-1]:
    print("¡La cadena es palíndroma!", cadena)
else:
    print("La cadena no es palíndroma")
