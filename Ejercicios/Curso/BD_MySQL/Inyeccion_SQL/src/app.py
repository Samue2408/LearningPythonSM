from db import get_connection

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        id = 3
        # No es recomendable de estas formas
        # query = "SELECT id, nombre FROM ciudades WHERE id = 3"
        # query = "SELECT id, nombre FROM ciudades WHERE id = {}".format(id)
        # query = f"SELECT id, nombre FROM ciudades WHERE id = {id}".format(id)

        # La forma correcta es 
        cursor.execute("SELECT id, nombre FROM ciudades WHERE id = %s", (int(id),)) # Se le pone el int para que si llega a encontrar una cadena de texto la elimine
        row = cursor.fetchone()
        print(row)
    connection.close()
except Exception as ex:
    print(ex)