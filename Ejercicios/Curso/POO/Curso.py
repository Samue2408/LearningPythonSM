class Curso:
    def __init__(self, nom, cre, pro):  # Constructor
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial" # Propiedad encapsulada siempre se les pone dos guiones bajos al principio

    def mostrarDatos(self):
        dat = "Nombre: {0} / Creditos: {1} / Modo de imparticion: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asignado".title())
        else:
            print("No existe docente asignado".title())

    def __verificarDocente(self):# Funcion encapsulada siempre se les pone dos guiones bajos al principio
        print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False
        
    def __str__(self): #Con este metodo, al impirmir print(curso1) realiza las instrucciones de este metodo
        texto = "Nombre: {0} | Creditos: {1}"
        return texto.format(self.nombre, self.creditos)
        

curso1 = Curso("Matematica", 5, "Ingenieria Civil")
print(curso1.mostrarDatos())

print(curso1)