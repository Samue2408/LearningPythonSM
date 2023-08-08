import mysql.connector
from mysql.connector import Error

print()
try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '31165833093Simm',
        db = 'ciudades'
    )

    if conexion.is_connected():
        print("Conexion exitosa")

        cursor = conexion.cursor()
        nombre = input("Ingrese una ciudad: ")
        alcalde = input("Ingrese su alcalde: ")
        pais = input("Ingrese el codigo del pais: ")

        #cursor.execute("INSERT INTO ciudades (nombre, alcalde, pais) VALUES ('MEDELLIN', 'PABON', '1')") # Permite realizar una sentencia SQL
        sentencia = "INSERT INTO ciudades (nombre, alcalde, pais) VALUES ('{0}', '{1}', {2})".format(nombre, alcalde, pais)
        cursor.execute(sentencia)
        conexion.commit() # Para confirmar la accion que estamos ejecutando
        print("Registro registrado con exito")

except Error as ex:
    print("Error durante la conexion")



finally:
    if conexion.is_connected():
        conexion.close() # Para cerrar la conexion
        print("Conexion cerrada")
        print()
