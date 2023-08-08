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
        cursor.execute("SELECT database();") # Permite realizar una sentencia SQL, esta especificamente es para saber el nombre de la base de datos
        registro = cursor.fetchone() # Aqui es donde se obtiene el resultado de la anterior sentencia, fecthone es cuanso es un solo resultado
        print("Conectado a la BD: ", registro)

        cursor.execute("SELECT * FROM paises")
        resultados = cursor.fetchall() # Aqui es donde se obtiene el resultado de la anterior sentencia, fecthall es cuando son varios resultados

        print()
        print("ID - PAIS - CAPITAL - PRESIDENTE")
        for fila in resultados:
            print(fila[0], fila[1], fila[2], fila[3], sep=" - ")
        print()

        print("Total de registros: ", cursor.rowcount)


except Error as ex:
    print("Error durante la conexion")



finally:
    if conexion.is_connected():
        conexion.close() # Para cerrar la conexion
        print("Conexion cerrada")
        print()
