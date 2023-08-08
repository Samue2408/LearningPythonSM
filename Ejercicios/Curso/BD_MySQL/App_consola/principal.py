from BD.conexion import DAO
from mysql.connector import Error
from funciones import *

def menuPrincipal():
    continuar = True
    while continuar:
        print("\n\n========== MENU PRINCIPAL ===========")
        print("1.- Listar ciudades")
        print("2.- Registrar ciudades")
        print("3.- Actualizar ciudades")
        print("4.- Eliminar ciudades")
        print("5.- Salir")
        print("=====================================")
        opcion = int(input("Indique el numero de su eleccion: "))
        print()

        if opcion < 1 or opcion > 5:
            print("Opcion incorecta, ingrese nuevamente...")
        elif opcion == 5:
            print("Gracias por usar este sistema!")
            continuar = False
        else:
            ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:

            ciu = dao.ListarCiudades()

            if len(ciu) > 0:
                listarCiudades(ciu)
            else:
                print("No se encontraron ciudades")

        except Error as e:
            print("Error en la conexion: ", e)

    elif opcion == 2:

        ciudad = pedirDatosCiudades()

        try:
            dao.registrarCiudad(ciudad)
        except Error as e:
            print("Error en la conexion: ")

    elif opcion == 3:
        
        try:
            print()
            ciu = dao.ListarCiudades()

            if len(ciu) > 0:
                ciudad = pedirDatosActuali(ciu)
                if ciudad:
                    dao.actualizarCiu(ciudad)
                else:
                    print("\nCodigo no encontrado...")
            else:
                print("No se encontraron ciudades")

        except Error as e:
            print("Error en la conexion: ")

    elif opcion == 4:

        try:
            print()
            ciu = dao.ListarCiudades()

            if len(ciu) > 0:
                codifoEliminar = pedirDatosElim(ciu)
                if not (codifoEliminar == ""):
                    dao.eliminarCiu(codifoEliminar)
                else:
                    print("\nCodigo no encontrado...")
            else:
                print("No se encontraron ciudades")

        except Error as e:
            print("Error en la conexion: ")


menuPrincipal()
