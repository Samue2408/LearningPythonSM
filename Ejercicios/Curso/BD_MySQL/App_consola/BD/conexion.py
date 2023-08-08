import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self) -> None:
        
        try:
            self.conexion = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '31165833093Simm',
            db = 'ciudades'
            )

        except Error as ex:
            print("Error durante la conexion: ", ex)

    def ListarCiudades(self):
        if self.conexion.is_connected():
            try:        
                cursor = self.conexion.cursor()
                cursor.execute("SELECT ciu.id, ciu.nombre, ciu.alcalde, pai.nombre FROM ciudades ciu, paises pai WHERE pai.id = ciu.pais ORDER BY ciu.nombre ASC") # PARA OBTENER LAS CIUDADES EN ORDEN ASCENDENTE POR EL NOMBRE ALFABETICAMENTE
                resultados = cursor.fetchall()
                print("Numero de registros: ", cursor.rowcount)
                return resultados
            
            except Error as ex:
                print("Error durante la conexion: ", ex)

    def registrarCiudad(self, ciud):
        if self.conexion.is_connected():

            try:        
                cursor = self.conexion.cursor()
                sentencia = "INSERT INTO ciudades (nombre, alcalde, pais) VALUES ('{0}', '{1}', {2})".format(ciud[0], ciud[1], ciud[2])
                cursor.execute(sentencia)
                self.conexion.commit() # Para confirmar la accion que estamos ejecutando
                print("\n¡Ciudad Registrada!")
            
            except Error as ex:
                print("Error durante la conexion: ", ex)

    
    def eliminarCiu(self, ciu):
        if self.conexion.is_connected():

            try:        
                cursor = self.conexion.cursor()
                sentencia = "DELETE FROM ciudades WHERE id = {}".format(ciu)
                cursor.execute(sentencia)
                self.conexion.commit() # Para confirmar la accion que estamos ejecutando
                print("\n¡Ciudad Eliminada!")
            
            except Error as ex:
                print("Error durante la conexion: ", ex)

    def actualizarCiu(self, ciu):
        if self.conexion.is_connected():

            try:        
                cursor = self.conexion.cursor()
                sentencia = "UPDATE ciudades SET nombre = '{0}', alcalde = '{1}', pais = {2} WHERE id = {3}".format(ciu[1], ciu[2], ciu[3], ciu[0])
                cursor.execute(sentencia)
                self.conexion.commit() # Para confirmar la accion que estamos ejecutando
                print("\n¡Ciudad Actualizada!")
            
            except Error as ex:
                print("Error durante la conexion: ", ex)
                