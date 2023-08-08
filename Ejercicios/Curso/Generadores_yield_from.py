def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng # Recorre caracter por caracter del elemento, cre un objeto iterable dentro de otro objeto iterable
        
        """
        #EL YIELD FORM REMPLAZA ESTA LINEA DE CODIGO
        for le in leng:
            yield le
        """

LenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript ")

print(next(LenguajesObtenidos))
print(next(LenguajesObtenidos))