CREATE DATABASE proyectointegradorv01;
USE proyectointegradorv01;

CREATE TABLE if not exists Estado(
Id_Estado int primary key not null auto_increment, 
Nombre_Estado varchar(20) not null
);
CREATE TABLE if not exists Tipo_Dispositivo(
Id_Modelo int primary key not null auto_increment,
Modelo varchar(50) not null
);

CREATE TABLE if not exists Dispositivos_IoT(
Id_Dispositivos int primary key not null auto_increment,
Id_Modelo varchar(50) not null,
Numero_de_serie varchar(30) not null,
Direccion_de_instalacion varchar(50),
Fecha_de_instalacion date,
Coordenadas varchar(30),
Id_Estado int,
FOREIGN KEY(Id_Estado) REFERENCES Estado(Id_EStado),
FOREIGN KEY(Id_Modelo) REFERENCES Tipo_Dispositivo(Id_Modelo)
);

