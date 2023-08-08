#SAMUEL MALDONADO MONTERO

# Pedimos al usuario que introduzca una cadena
cadena = input("Introduce una palabra o frase: ")
# Convertimos la cadena a minúsculas y eliminamos los espacios en blanco
cadena = cadena.lower().replace(" ", "")

# Comprobamos si es palíndroma y mostramos un mensaje adecuado
if cadena == cadena[::-1]:
    print("¡La cadena es palíndroma!", cadena)
else:
    print("La cadena no es palíndroma.")