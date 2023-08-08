class Pais():

    def __init__(self,nom, pre):
        self.nombre = nom 
        self.presidente = pre

    def __str__(self) -> str:
        txt = "Pais: {0} - Presidente: {1}"
        return txt.format(self.nombre, self.presidente)


class Ciudad():

    def __init__(self, nom, hab, pai) -> None:
        self.nombre = nom
        self.habitantes = hab
        self.pais = pai

    def __str__(self) -> str:
        txt = "Ciudad: {0} - N° Habitantes: {1} ({2})"
        return txt.format(self.nombre, self.habitantes, self.pais)



    
class Urbanizacion():

    def __init__(self, nom, ciu) -> None:
        self.nombre = nom
        self.ciudad = ciu

    def __str__(self) -> str:
        txt = "Urbanizacion: {0} ({1})"
        return txt.format(self.nombre, self.ciudad)

pais1 = Pais("Colombia", "Petro")
print(pais1)

ciudad1 = Ciudad("Barranquilla", 2150000, pais1) # herencia
print(ciudad1)

urbani = Urbanizacion("San Isidro", ciudad1) # Herencia
print(urbani)