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

        cursor.execute("UPDATE ciudades SET nombre = 'Medellin', alcalde = 'Pabon' WHERE id = 6") # Permite realizar una sentencia SQL
        
        conexion.commit() # Para confirmar la accion que estamos ejecutando
        print("Actualizacion con exito")

except Error as ex:
    print("Error durante la conexion")



finally:
    if conexion.is_connected():
        conexion.close() # Para cerrar la conexion
        print("Conexion cerrada")
        print()
