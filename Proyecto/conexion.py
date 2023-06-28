import mysql.connector

class Conexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión")

    def leer_Dispositivos_IoT(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM Dispositivos_IoT"
            cursor.execute(query)
            dispositivos = cursor.fetchall()
            cursor.close()
            return dispositivos
        else:
            print("No hay conexión a la base de datos")

    def InsertarDispositivo(self, Id_Modelo, Numero_de_serie, Direccion_de_instalacion, Fecha_de_instalacion, Coordenadas, Id_Estado):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO Dispositivos_IoT (Id_Modelo, Numero_de_serie, Direccion_de_instalacion, Fecha_de_instalacion, Coordenadas, Id_Estado)  VALUES (%s, %s, %s, %s, %s, %s)"
            datos = (Id_Modelo, Numero_de_serie, Direccion_de_instalacion, Fecha_de_instalacion, Coordenadas, Id_Estado)
            cursor.execute(query, datos)
            self.connection.commit()
            cursor.close()
            print("Datos insertados correctamente")
        else:
            print("No hay conexión a la base de datos")

    def EliminarDispositivo(self, Id_Dispositivo):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "DELETE FROM Dispositivos_IoT WHERE Id_Dispositivo = %s"
            datos = (Id_Dispositivo,)
            cursor.execute(query, datos)
            self.connection.commit()
            cursor.close()
            print("Dispositivo eliminado correctamente")
        else:
            print("No hay conexión a la base de datos")


    def ActualizarDispositivo(self, modelo_nuevo, numero_serie_nuevo, estado_nuevo, id_dispositivo):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "UPDATE Dispositivos_Iot SET Id_Modelo = %s, Numero_de_serie = %s, Id_Estado = %s WHERE Id_Dispositivos = %s"
            values = (modelo_nuevo, numero_serie_nuevo, estado_nuevo, id_dispositivo)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Dispositivo actualizado correctamente")
        else:
            print("No hay conexión a la base de datos")


            
    def leer_DispositivosXTipo(self):
        if  self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM Tipo_Dispositivo"
            cursor.execute(query)
            dispositivos = cursor.fetchall()
            cursor.close()
            return dispositivos     
        else:
            print("No hay conexión a la base de datos")
            
            
    def leer_DispositivosXEstado(self):
        if  self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM Estado"
            cursor.execute(query)
            dispositivos = cursor.fetchall()
            cursor.close()
            return dispositivos     
        else:
            print("No hay conexión a la base de datos")