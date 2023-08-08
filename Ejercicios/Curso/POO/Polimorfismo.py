#Polimorfismo: 

class Estudiante():

    def describir(self):
        print("Soy un buen estudiante")


class Docente():

    def describir(self):
        print("Me dedico a enseñar cursos")


class Trabajador():

    def describir(self):
        print("Trabajo dentro de una gran empresa")

def describirPersona(Persona):
    Persona.describir()

doc1 = Estudiante()
describirPersona(doc1)
    
    