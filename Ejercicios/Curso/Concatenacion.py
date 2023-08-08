texto1 = "Hola"
texto2 = "Mundo"

    #primera manera
textoFinal = texto1 + " " + texto2
print(textoFinal)

    #segunda manera
print("El saludo es: %s %s" % (texto1, texto2))

    #tercera forma
#saludoFinal = "Saludo: {0} {1}".format(texto1, texto2) 
saludoFinal = "Saludo: {} {}".format(texto1, texto2) 
print(saludoFinal)

    #cuarta forma
saludoFinal2 = "Saludo es: {x} {y}".format(x=texto1, y=texto2) 
print(saludoFinal2)