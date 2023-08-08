def listarCiudades(ciu):
    print()
    print("ID\tCIUDAD\tALCALDE\tPAIS")

    for fila in ciu:
        print(fila[0], fila[1], fila[2], fila[3], sep="\t")
        print()


def pedirDatosCiudades():
    correcto = False
    while not correcto:
        nombre = input("Ingrese una ciudad: ")
        alcalde = input("Ingrese su alcalde: ")
        pais = input("Ingrese el codigo del pais: ")

        if len(nombre) <= 20:
            if len(alcalde) <= 20:
                if pais.isnumeric() and int(pais) > 0:
                    correcto = True
                else:
                    print("El codigo del pais debe ser un numero natural")
            else:
                print("Nombre de alcalde excede numero de caracteres (20)")
        else:
            print("Nombre ciudad excede numero de caracteres (20)")

    ciu = (nombre, alcalde, pais)

    return ciu


def pedirDatosElim(ciudad):

    listarCiudades(ciudad)
    codigoEliminar = int(input("\nIngrese el codigo de la ciudad a eliminar: "))
    existecodigo = False

    for ciu in ciudad:
        if ciu[0] == codigoEliminar:
            existecodigo = True
            break
    
    if not existecodigo:
        codigoEliminar = ""

    return codigoEliminar

def pedirDatosActuali(ciudad):
    listarCiudades(ciudad)
    print()
    codigoEditar = int(input("\nIngrese el codigo de la ciudad a editar: "))
    existecodigo = False

    for ciu in ciudad:
        if ciu[0] == codigoEditar:
            existecodigo = True
            break
    
    if existecodigo:
        datosDados = pedirDatosCiudades()
        datos = (codigoEditar, datosDados[0], datosDados[1], datosDados[2])
    else: 
        datos = None

    return datos