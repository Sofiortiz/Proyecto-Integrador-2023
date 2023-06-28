import conexion

    

def mostrar_menu_dispositivos():
    print("             MENU DISPOSITIVOS          ")
    print("Elija una opcion ingresando el numero correspondiente")
    print("1_ Actualizar dispositivo")
    print("2_ Insertar un nuevo dispositivo")
    print("3_ Eliminar un dispositivo")



def ActualizarDispositivo():
    # Pedir datos del dispositivo a actualizar
    id_dispositivo = int(input("Ingrese el ID del dispositivo a actualizar: "))
    modelo_nuevo = str(input("Ingrese el nombre del nuevo modelo de dispositivo: ")) 
    numero_serie_nuevo = str(input("Ingrese el numero de serie del nuevo dispositivo: "))
    estado_nuevo = str(input("Ingrese el estado del dispositivo:  "))

    # Crear una instancia del conector de base de datos
    conexion_bd = conexion.Conexion(host="localhost", user="root", password="root", database="proyectointegradorv01")

    # Conectar a la base de datos
    conexion_bd.connect()

    # Actualizar el dispositivo en la base de datos
    conexion_bd.actualizar_dispositivo(modelo_nuevo, numero_serie_nuevo, estado_nuevo, id_dispositivo)

    # Desconectar de la base de datos
    conexion_bd.disconnect()

    print("Dispositivo actualizado correctamente")
    

def InsertarDispositivo():
    # Pedir datos del nuevo dispositivo
    Id_Modelo = str(input("Ingrese el modelo del nuevo dispositivo: "))
    Numero_de_serie = str(input("Ingrese el número de serie del nuevo dispositivo: "))
    Id_estado = str(input("Ingrese el estado del nuevo dispositivo: "))

    # Crear una instancia del conector de base de datos
    conexion_bd = conexion.Conexion(host="localhost", user="root", password="root", database="proyectointegradorv01")

    # Conectar a la base de datos
    conexion_bd.connect()

    # Insertar el dispositivo en la base de datos
    conexion_bd.InsertarDispositivo(Id_Modelo, Numero_de_serie, Id_estado)

    # Desconectar de la base de datos
    conexion_bd.disconnect()

    print("Dispositivo insertado correctamente")

def EliminarDispositivo():
    # Pedir datos del dispositivo a eliminar
    Id_Dispositivo = str(input("Ingrese el id del dispositivo a eliminar: "))

    # Crear una instancia del conector de base de datos
    conexion_bd = conexion.Conexion(host="localhost", user="root", password="root", database="proyectointegradorv01")

    # Conectar a la base de datos
    conexion_bd.connect()

    # Insertar el dispositivo en la base de datos
    conexion_bd.InsertarDispositivo(Id_Dispositivo)

    # Desconectar de la base de datos
    conexion_bd.disconnect()

    print("Dispositivo eliminado correctamente")
    

    
# Mostrar el menú y solicitar la opción al usuario
mostrar_menu_dispositivos()

opcion_menu =int (input("Ingrese la opción deseada: "))

if opcion_menu == 1:
    ActualizarDispositivo()

elif opcion_menu == 2:
    InsertarDispositivo()

else:
    EliminarDispositivo()