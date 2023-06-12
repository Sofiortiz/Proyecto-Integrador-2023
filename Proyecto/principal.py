import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Conexion(host="localhost", user="root", password="hernan2023", database="proyectointegradorv01")

# Conectar a la base de datos
conexion_bd.connect()

# Cargar Dispositivos en la tabla
conexion_bd.InsertarDispositivos(Id_Dispositivos= 1 ,Id_Modelo= 1, Numero_de_serie= "AXCT", Direccion_de_instalacion="Punilla", Fecha_de_instalacion="2019-04-01", Coordenadas="DEco", Id_Estado= 1)

 # Leer los Dispositivos desde la tabla
dispositivos = conexion_bd.leer_Dispositivos_IoT()
for ListaDispositivos in dispositivos:
 print(ListaDispositivos)
   
   
print("Listado de dispositivos totales.")
   
#Listado de dispositivos por tipo.

dispositivosXTIPO = conexion_bd.leer_DispositivosXTipo()
for ListaXtipo in dispositivosXTIPO:
   
 print(ListaXtipo)
 
 
 
 
print("Listado de dispositivos por tipo.")
   


#Listado de dispositivos por estado.

dispositivosXESTADO = conexion_bd.leer_DispositivosXEstado()
for ListaXEstado in dispositivosXESTADO:
  
 print(ListaXEstado)






print("Listado de dispositivos por estado.")


# Desconectar de la base de datos
conexion_bd.disconnect()