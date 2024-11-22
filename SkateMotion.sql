CREATE DATABASE SkateMotion;

USE SkateMotion;

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
    categoria VARCHAR(100),
    rutaImagen VARCHAR(100)
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

INSERT INTO Tipos_Usuario(idTipo, descripcion) VALUES
(1, 'administrador'),
(2, 'usuario');

INSERT INTO Usuarios(idUsuario, nombre, contra, correo, idTipo) VALUES
(1, 'Admin', '123', 'admin@gmail.com', '1'),
(2, 'Pablo Castillo', 'pablo', 'pablo@gmail.com', '2'),
(3, 'Diego Martinez', 'diego', 'diego@gmail.com', '2'),
(4, 'Arturo Vargas', 'arturo', 'arturo@gmail.com', '2'),
(5, 'Maria Lopez', 'maria', 'maria@gmail.com', '2'),
(6, 'Juan Perez', 'juan', 'juan@gmail.com', '2'),
(7, 'Ana Torres', 'ana', 'ana@gmail.com', '2'),
(8, 'Luis Fernandez', 'luis', 'luis@gmail.com', '2'),
(9, 'Carla Gomez', 'carla', 'carla@gmail.com', '2'),
(10, 'Miguel Sanchez', 'miguel', 'miguel@gmail.com', '2');

INSERT INTO Productos(idProducto, nombre, precio, inventarioProducto, categoria, rutaImagen) VALUES
(1, 'DGK Overlord Tabla', 1200, 10, 'Tabla', 'OverloadTabla'),
(2, 'POWELL Caballero Dragon Tabla',1000, 12, 'Tabla', 'CaballeroTabla'),
(3, 'POWELL Gundam Tabla',1000, 14, 'Tabla', 'GundamTabla'),
(4, 'POWELL Sakura Tiger Tabla',1000, 20, 'Tabla', 'SakuraTabla'),
(5, 'Real Wair Illuminated Tabla',1500, 5, 'Tabla', 'WairTabla'),
(6, 'Hamaguchi Aloha Tabla',1400, 10, 'Tabla', 'AlohaTabla'),
(7, 'Ace AF1 Eje', 600, 10, 'Eje', 'AF1Eje'),
(8, 'Ace AF1 LTD Black Eje', 700, 5, 'Eje', 'AF1BlackEje'),
(9, 'Bullet Standard Eje', 300, 8, 'Eje', 'BulletStandardEje'),
(10,'Independent S11 Hollow Fabiana Eje', 600, 4, 'Eje', 'S11HollowEje'),
(11,'Independent S11 Hollow IKP Eje', 640, 5, 'Eje', 'S11ForgedHollowIKPEje'),
(12,'Krux K5 Standard Eje', 400, 9, 'Eje', 'KruxK5Eje'),
(13,'Bones X-Formula V7 Ruedas', 420, 10, 'Rueda', 'XFormulaV7Ruedas'),
(14,'Bones X-Formula Dino Ruedas', 420, 6, 'Rueda', 'XFormulaDinoRuedas'),
(15,'Darkstar Responder Ruedas', 300, 5, 'Rueda', 'DarkstartRuedas'),
(16,'Bones X-Formula Look Book Ruedas', 440, 6, 'Rueda', 'LookBookRuedas'),
(17,'OJ Double Duro Ruedas', 1000, 2, 'Rueda', 'DoubleDuroRuedas'),
(18,'OJ Ace Pelka Ruedas', 1100, 4, 'Rueda', 'AcePelkaRuedas'),
(19,'Alien Workshop Spectrum Completa', 2200, 3, 'Completa', 'SpectrumCompleta'),
(20,'Birdhouse Flying Falcon Completa', 2000, 4, 'Completa', 'FlyingFalconCompleta'),
(21,'Birdhouse Lizzie Butterfly Completa', 2000, 3, 'Completa', 'LizzieCompleta'),
(22,'Santa Cruz Classic Dot Black Completa', 1100, 5, 'Completa', 'DotBlackCompleta'),
(23,'Santa Cruz Classic Dot Green Completa', 1100, 6, 'Completa', 'DotGreenCompleta'),
(24,'POWELL Peralta Dragon Completa', 1500, 4, 'Completa', 'PeraltaDragonCompleta');

INSERT INTO Proveedores(idProveedor, nombreProveedor, telefonoProveedor, correoProveedor, dirProveedor) VALUES
(1, 'DGK', '8112838182', 'dgk@gmail.com', 'Calle Los Cabos 104'),
(2, 'POWELL', '818458285', 'powell@gmail.com', 'Calle Nubes Triunfantes 934'),
(3, 'Real Skateboards', '8123456789', 'real@gmail.com', 'Avenida Real 123'),
(4, 'Independent Trucks', '8198765432', 'independent@gmail.com', 'Boulevard Independencia 456'),
(5, 'Krux Trucks', '8112345678', 'krux@gmail.com', 'Calle Krux 789'),
(6, 'Spitfire Wheels', '8187654321', 'spitfire@gmail.com', 'Avenida Spitfire 101'),
(7, 'Bones Bearings', '8123456780', 'bones@gmail.com', 'Calle Bones 202'),
(8, 'Santa Cruz', '8198765430', 'santacruz@gmail.com', 'Boulevard Santa Cruz 303'),
(9, 'Element Skateboards', '8123456781', 'element@gmail.com', 'Calle Element 404'),
(10, 'Birdhouse Industries', '8198765431', 'bidhouse@gmail.com', 'Avenida Globe 505');

INSERT INTO Compras(idCompra, fecha, idUsuario) VALUES 
(1, CURDATE(), 1),
(2, CURDATE(), 1),
(3, CURDATE(), 2),
(4, CURDATE(), 3),
(5, CURDATE(), 4),
(6, CURDATE(), 4),
(7, CURDATE(), 4),
(8, CURDATE(), 8),
(9, CURDATE(), 9),
(10, CURDATE(), 10);

INSERT INTO Contiene(idProducto, idCompra, cantidad) VALUES
(1,1,2),
(20,1,1),
(13,2,2),
(5,3,1),
(19,4,1),
(11,5,2),
(21,6,2),
(7,6,1),
(3,7,3),
(16,8,1),
(9,9,3),
(18,10,2);

INSERT INTO Proveedores_Compras(idCompraProveedor, fecha, idProveedor) VALUES
(1, CURDATE(), 1),
(2, CURDATE(), 2),
(3, CURDATE(), 3),
(4, CURDATE(), 4),
(5, CURDATE(), 5),
(6, CURDATE(), 6),
(7, CURDATE(), 7),
(8, CURDATE(), 8),
(9, CURDATE(), 9),
(10, CURDATE(), 10);

INSERT INTO Viene_De(idProducto, idCompraProveedor, precioProveedor, cantidad) VALUES
(1, 1, 600, 10),
(2, 2, 500, 12),
(3, 2, 500, 14),
(4, 2, 500, 20),
(5, 5, 750, 5),
(6, 6, 700, 10),
(7, 7, 300, 10),
(8, 8, 350, 5),
(9, 9, 150, 8),
(10, 10, 300, 4),
(11, 1, 320, 5),
(12, 2, 200, 9),
(13, 3, 210, 10),
(14, 4, 210, 6),
(15, 5, 150, 5),
(16, 6, 220, 6),
(17, 7, 500, 2),
(18, 8, 550, 4),
(19, 9, 1100, 3),
(20, 10, 1000, 4),
(21, 1, 1000, 3),
(22, 2, 550, 5),
(23, 3, 550, 6),
(24, 4, 750, 4);


--Stored procedure para registrar usuario
DELIMITER $$
CREATE PROCEDURE registrarUsuario(
    IN nom VARCHAR(255),
    IN con VARCHAR(255),
    IN cor VARCHAR(255)
)
BEGIN 
    DECLARE usuario_existente INT DEFAULT 0;
    SELECT COUNT(*) INTO usuario_existente FROM Usuarios WHERE correo = cor;
    IF usuario_existente = 0 THEN
        INSERT INTO Usuarios(nombre, contra, correo) VALUES(nom, con, cor);
    ELSE 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Usuario existente';
    END IF;
END $$
DELIMITER ;

--Stored procedure para login de un usuario que regresa la id si existe
DELIMITER $$
CREATE PROCEDURE loginUsuario(
    IN cor VARCHAR(255),
    IN con VARCHAR(255)
)
BEGIN
    SELECT idUsuario FROM Usuarios WHERE correo = cor AND contra = con;
END $$
DELIMITER;

-- Stored procedure para ver productos por tipo
DELIMITER $$
CREATE PROCEDURE productosPorTipo(
    IN tipo VARCHAR(100)
)
BEGIN
    SELECT * FROM Productos WHERE categoria = tipo;
END $$

--Select Para ver productos y sus proveedores
SELECT prod.nombre, prov.nombreProveedor 
FROM Productos prod JOIN Viene_De  vi ON prod.idProducto = vi.idProducto 
JOIN Proveedores_Compras pc ON vi.idCompraProveedor = pc.idCompraProveedor
JOIN Proveedores prov ON pc.idProveedor = prov.idProveedor;

--Stored procedure para insertar compra
DELIMITER $$
CREATE PROCEDURE compra(
    IN 
    IN
    IN

)