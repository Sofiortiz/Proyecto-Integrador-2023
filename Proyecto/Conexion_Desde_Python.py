import mysql.connector
midb = mysql.connector.connect(
host="localhost",
user="usuario",
password="contraseña",
database="NombreDeBaseDatos"
)
print(midb)