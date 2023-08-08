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
        infoServer = conexion.get_server_info()
        print("Informacion del servidor: ", infoServer)
except Error as ex:
    print("Error durante la conexion")
finally:
    if conexion.is_connected():
        conexion.close() # Para cerrar la conexion
        print("Conexion cerrada")
        print()
