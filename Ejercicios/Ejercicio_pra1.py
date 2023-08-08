nom = input("Ingrese el nombre del trabajador ")
key_dpto = int(input("Ingrese la Clave del departamento al que pertenece "))
antig = int(input("Ingrese la antiguedad del trabajador "))

if key_dpto == 1:
    if antig == 1:
        print("El trabajador " + nom + " tiene derecho a 6 dias de vacaciones")
    elif antig >= 2 and antig <=6:
        print("El trabajador " + nom + " tiene derecho a 14 dias de vacaciones")
    elif antig >= 7:
        print("El trabajador " + nom + " tiene derecho a 20 dias de vacaciones")

elif key_dpto == 2:
    if antig == 1:
        print("El trabajador " + nom + " tiene derecho a 7 dias de vacaciones")
    elif antig >= 2 and antig <=6:
        print("El trabajador " + nom + " tiene derecho a 15 dias de vacaciones")
    elif antig >= 7:
        print("El trabajador " + nom + " tiene derecho a 22 dias de vacaciones")

elif key_dpto == 3:
    if antig == 1:
        print("El trabajador " + nom + " tiene derecho a 10 dias de vacaciones")
    elif antig >= 2 and antig <=6:
        print("El trabajador " + nom + " tiene derecho a 20 dias de vacaciones")
    elif antig >= 7:
        print("El trabajador " + nom + " tiene derecho a 30 dias de vacaciones")
else:
    print("Clave del departamento incorrecta")
