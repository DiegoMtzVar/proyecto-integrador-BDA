CREATE DATABASE SkateMotion;

CREATE TABLE Tipos_Usuario(
    idTipo INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100)
);

CREATE TABLE Usuarios(
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    contra VARCHAR(255),
    correo VARCHAR(255) UNIQUE,
    idTipo INT DEFAULT 2,
    FOREIGN KEY (idTipo) REFERENCES Tipos_Usuario(idTipo)
);

CREATE TABLE Productos(
    idProducto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    precio INT,
    inventarioProducto INT,
    categoria VARCHAR(100)
);

CREATE TABLE Proveedores(
    idProveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombreProveedor VARCHAR(255),
    telefonoProveedor VARCHAR(20),
    correoProveedor VARCHAR(255) UNIQUE,
    dirProveedor VARCHAR(255)
);

CREATE TABLE Compras(
    idCompra INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    totalCompra INT,
    idUsuario INT,
    FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUsuario)
);

CREATE TABLE Contiene(
    idProducto INT,
    idCompra INT,
    cantidad INT,
    PRIMARY KEY (idProducto, idCompra),
    FOREIGN KEY (idCompra) REFERENCES Compras(idCompra),
    FOREIGN KEY (idProducto) REFERENCES Productos(idProducto)
);

CREATE TABLE Proveedores_Compras(
    idCompraProveedor INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    total INT,
    idProveedor INT,
    FOREIGN KEY (idProveedor) REFERENCES Proveedores(idProveedor)
);

CREATE TABLE Viene_De(
    idProducto INT,
    idCompraProveedor INT,
    precioProveedor INT,
    cantidad INT,
    PRIMARY KEY (idProducto, idCompraProveedor),
    FOREIGN KEY (idCompraProveedor) REFERENCES Proveedores_Compras(idCompraProveedor),
    FOREIGN KEY (idProducto) REFERENCES Productos(idProducto)
);

