import mysql.connector
midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="prueba_proyecto"
)
print(midb)

cursor=midb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)