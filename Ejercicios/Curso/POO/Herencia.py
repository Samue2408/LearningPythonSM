class Persona:  # Clase Padre
    def __init__(self, nom, apePat, apeMat):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostratNombreCompleto(self):
        txt = "{0} {1} {2}"
        return txt.format(self.nombres, self.apellidoPaterno, self.apellidoMaterno)

    def datos(self):
        print(self.mostratNombreCompleto())


class Estudiante(Persona):  # Para heredar - Clase hija
    def __init__(self, nom, apePat, apeMat, pro):
        super().__init__(nom, apePat, apeMat)
        self.profesion = pro

    def datos(self):  # Esto es parecido a un override
        super().datos()
        print(self.profesion)


est1 = Estudiante("Samuel", "Maldonado", "Montero", "Ingeniero de Sitemas")
#est1.datos()

print(isinstance(est1, Persona)) # Para saber si un objeto es instancia de una clase