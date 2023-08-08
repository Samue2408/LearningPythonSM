class persona:
    apellidos = ""
    nombres = ""
    edad = 0
    despierto = False

    def despertar(
        self,
    ):  # self:parametro que hace referencia a la instancia perteneciente a la clase
        print("Buen Dia")
        self.despierto = True


persona1 = persona()

persona1.apellidos = "Maldonado Montero"

print(persona1.apellidos)
print(persona1.despierto)
persona1.despertar()
print(persona1.despierto)

persona2 = persona()

persona2.apellidos = "Paz Torres"

print(persona2.apellidos)
print(persona2.despierto)
persona2.despertar()
print(persona2.despierto)
