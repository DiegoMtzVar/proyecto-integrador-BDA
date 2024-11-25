CREATE USER IF NOT EXISTS 'skatemotion'@'localhost' IDENTIFIED BY 'skatemotion';
GRANT ALL PRIVILEGES ON *.* TO 'skatemotion'@'localhost';

DROP DATABASE IF EXISTS SkateMotion;

CREATE DATABASE SkateMotion;

USE SkateMotion;

CREATE TABLE Tipos_Usuario(
    idTipo INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100)
);

CREATE TABLE Tipos_Status(
    idStatus INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100)
);

CREATE TABLE Tipos_Envios(
    idEnvio INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100)
);
CREATE TABLE Tipos_Categorias(
    idCategoria INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100)
);

CREATE TABLE Cupones(
    codigoCupon VARCHAR(10),
    descuento INT,
    activo BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (codigoCupon)
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
    idCategoria INT,
    rutaImagen VARCHAR(100),
    FOREIGN KEY (idCategoria) REFERENCES Tipos_Categorias(idCategoria)
);

CREATE TABLE Proveedores(
    idProveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombreProveedor VARCHAR(255),
    telefonoProveedor VARCHAR(20),
    correoProveedor VARCHAR(255) UNIQUE,
    dirProveedor VARCHAR(255)
);

CREATE TABLE Ventas(
    idCompra INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE DEFAULT CURDATE(),
    fecha_entrega DATE,
    direccion text,
    idUsuario INT,
    idStatus INT DEFAULT 1,
    idEnvio INT,
    codigoCupon VARCHAR(10),
    FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUsuario),
    FOREIGN KEY (idStatus) REFERENCES Tipos_Status(idStatus),
    FOREIGN KEY (idEnvio) REFERENCES Tipos_Envios(idEnvio),
    FOREIGN KEY (codigoCupon) REFERENCES Cupones(codigoCupon)
);

CREATE TABLE Contiene(
    idProducto INT,
    idCompra INT,
    cantidad INT,
    PRIMARY KEY (idProducto, idCompra),
    FOREIGN KEY (idCompra) REFERENCES Ventas(idCompra),
    FOREIGN KEY (idProducto) REFERENCES Productos(idProducto)
);

CREATE TABLE Compras(
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
    FOREIGN KEY (idCompraProveedor) REFERENCES Compras(idCompraProveedor),
    FOREIGN KEY (idProducto) REFERENCES Productos(idProducto)
);

CREATE TABLE Resenas(
    idReseña INT AUTO_INCREMENT PRIMARY KEY,
    idUsuario INT,
    idProducto INT,
    calificacion INT,
    comentario VARCHAR(255),
    FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUsuario),
    FOREIGN KEY (idProducto) REFERENCES Productos(idProducto)
);

INSERT INTO Tipos_Usuario(idTipo, descripcion) VALUES
(1, 'administrador'),
(2, 'usuario');

INSERT INTO Tipos_Envios(idEnvio, descripcion) VALUES
(1, 'Normal'),
(2, 'Flash'),
(3, 'Express');

INSERT INTO Tipos_Status(idStatus, descripcion) VALUES
(1, 'Pendiente'),
(2, 'En bodega'),
(3, 'En camino'),
(4, 'Entregado');

INSERT INTO Tipos_Categorias(idCategoria, descripcion) VALUES
(1, 'Tabla'),
(2, 'Eje'),
(3, 'Rueda'),
(4, 'Completa');

INSERT INTO Usuarios(idUsuario, nombre, contra, correo, idTipo) VALUES
(1, 'Admin', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'admin@gmail.com', '1'),
(2, 'Pablo Castillo', '26079e41910bcde04be636fbeecc9045379882b5ad3fe7f70b762436c6d98055', 'pablo@gmail.com', '2'),
(3, 'Diego Martinez', '00e48a815525529ba9d33f8761a167588fe00c47bc82f515cf791c482ed99ecc', 'diego@gmail.com', '2'),
(4, 'Arturo Vargas', '11cdf86d5723eecce5af1f33e5fde9f066e608d0a1068f445d99820eef5c19ae', 'arturo@gmail.com', '2'),
(5, 'Maria Lopez', '94aec9fbed989ece189a7e172c9cf41669050495152bc4c1dbf2a38d7fd85627', 'maria@gmail.com', '2'),
(6, 'Juan Perez', 'ed08c290d7e22f7bb324b15cbadce35b0b348564fd2d5f95752388d86d71bcca', 'juan@gmail.com', '2'),
(7, 'Ana Torres', '24d4b96f58da6d4a8512313bbd02a28ebf0ca95dec6e4c86ef78ce7f01e788ac', 'ana@gmail.com', '2'),
(8, 'Luis Fernandez', 'c5ff177a86e82441f93e3772da700d5f6838157fa1bfdc0bb689d7f7e55e7aba', 'luis@gmail.com', '2'),
(9, 'Carla Gomez', '8813d406421e0063ef8ec81fc45170338b4cfd9547ee1ab157b90b46bcb6e2a7', 'carla@gmail.com', '2'),
(10, 'Miguel Sanchez', '5ef68465886fa04d3e0bbe86b59d964dd98e5775e95717df978d8bedee6ff16c', 'miguel@gmail.com', '2');

INSERT INTO Productos(idProducto, nombre, precio, inventarioProducto, idCategoria, rutaImagen) VALUES
(1, 'DGK Overlord Tabla', 1200, 10, 1, 'OverlordTabla.webp'),
(2, 'POWELL Caballero Dragon Tabla', 1000, 12, 1, 'CaballeroTabla.webp'),
(3, 'POWELL Gundam Tabla', 1000, 14, 1, 'GundamTabla.webp'),
(4, 'POWELL Sakura Tiger Tabla', 1000, 20, 1, 'SakuraTabla.webp'),
(5, 'Real Wair Illuminated Tabla', 1500, 5, 1, 'WairTabla.webp'),
(6, 'Element Aloha Tabla', 1400, 10, 1, 'AlohaTabla.webp'),
(7, 'Krux AF1 Eje', 600, 10, 2, 'AF1Eje.webp'),
(8, 'Krux AF1 LTD Black Eje', 700, 5, 2, 'AF1BlackEje.webp'),
(9, 'Independent Standard Eje', 300, 8, 2, 'BulletStandardEje.webp'),
(10, 'Independent S11 Hollow Fabiana Eje', 600, 4, 2, 'S11HollowEje.webp'),
(11, 'Independent S11 Hollow IKP Eje', 640, 5, 2, 'S11ForgedHollowIKPEje.webp'),
(12, 'Krux K5 Standard Eje', 400, 9, 2, 'KruxK5Eje.webp'),
(13, 'Bones X-Formula V7 Ruedas', 420, 10, 3, 'XFormulaV7Ruedas.webp'),
(14, 'Bones X-Formula Dino Ruedas', 420, 6, 3, 'XFormulaDinoRuedas.webp'),
(15, 'Element Responder Ruedas', 300, 5, 3, 'DarkstarRuedas.webp'),
(16, 'Bones X-Formula Look Book Ruedas', 440, 6, 3, 'LookBookRuedas.webp'),
(17, 'Spitfire Double Duro Ruedas', 1000, 2, 3, 'DoubleDuroRuedas.webp'),
(18, 'Spitfire Ace Pelka Ruedas', 1100, 4, 3, 'AcePelkaRuedas.webp'),
(19, 'Element Alien Workshop Spectrum Completa', 2200, 3, 4, 'SpectrumCompleta.webp'),
(20, 'Birdhouse Flying Falcon Completa', 2000, 4, 4, 'FlyingFalconCompleta.webp'),
(21, 'Birdhouse Lizzie Butterfly Completa', 2000, 3, 4, 'LizzieCompleta.webp'),
(22, 'Santa Cruz Classic Dot Black Completa', 1100, 5, 4, 'DotBlackCompleta.webp'),
(23, 'Santa Cruz Classic Dot Green Completa', 1100, 6, 4, 'DotGreenCompleta.webp'),
(24, 'POWELL Peralta Dragon Completa', 1500, 4, 4, 'PeraltaDragonCompleta.webp');

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

INSERT INTO Ventas(idCompra, fecha, direccion, idStatus, idUsuario, idEnvio, fecha_entrega) VALUES 
(1, CURDATE(), 'Mexico, CDMX, Polanco, Venustiano Carranza #123, 03100', 4, 1, 1, CURDATE() + INTERVAL 5 DAY),
(2, CURDATE(), 'Mexico, CDMX, Polanco, Insurgentes Sur #456, 03100', 4, 1, 2, CURDATE() + INTERVAL 3 DAY),
(3, CURDATE(), 'Mexico, Jalisco, Guadalajara, Benito Juarez #456, 44100', 4, 2, 3, CURDATE() + INTERVAL 1 DAY),
(4, CURDATE(), 'Mexico, Nuevo Leon, Monterrey, Venustiano Carranza #789, 64000', 4, 3, 1, CURDATE() + INTERVAL 5 DAY),
(5, CURDATE(), 'Mexico, Yucatan, Merida, Benito Juarez #101, 97000', 1, 4, 2, CURDATE() + INTERVAL 3 DAY),
(6, CURDATE(), 'Mexico, Yucatan, Merida, Paseo de Montejo #202, 97000', 2, 4, 3, CURDATE() + INTERVAL 1 DAY),
(7, CURDATE(), 'Mexico, Yucatan, Merida, Calle 60 #303, 97000', 3, 4, 1, CURDATE() + INTERVAL 5 DAY),
(8, CURDATE(), 'Mexico, Puebla, Puebla, Venustiano Carranza #202, 72000', 4, 8, 2, CURDATE() + INTERVAL 3 DAY),
(9, CURDATE(), 'Mexico, Veracruz, Veracruz, Benito Juarez #303, 91700', 4, 9, 3, CURDATE() + INTERVAL 1 DAY),
(10, CURDATE(), 'Mexico, Quintana Roo, Cancun, Venustiano Carranza #404, 77500', 4, 10, 1, CURDATE() + INTERVAL 5 DAY);

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

INSERT INTO Compras(idCompraProveedor, fecha, idProveedor) VALUES
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
(5, 3, 750, 5),
(6, 9, 700, 10),
(7, 5, 300, 10),
(8, 5, 350, 5),
(9, 4, 150, 8),
(10, 4, 300, 4),
(11, 4, 320, 5),
(12, 5, 200, 9),
(13, 7, 210, 10),
(14, 7, 210, 6),
(15, 9, 150, 5),
(16, 7, 220, 6),
(17, 6, 500, 2),
(18, 6, 550, 4),
(19, 9, 1100, 3),
(20, 10, 1000, 4),
(21, 10, 1000, 3),
(22, 8, 550, 5),
(23, 8, 550, 6),
(24, 2, 750, 4);

--STORED PROCEDURES
--Stored procedure para login de un usuario que regresa la id y el rol si existe
DELIMITER $$
CREATE PROCEDURE loginUsuario(
    IN cor VARCHAR(255),
    IN con VARCHAR(255)
)
BEGIN
    SELECT idUsuario as ID, 
    descripcion as role 
    FROM Usuarios u JOIN Tipos_Usuario t ON u.idTipo = t.idTipo 
    WHERE correo = cor AND contra = con;
END $$
DELIMITER ;

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

--Stored procedure para obtener todos los usuarios
DELIMITER $$
CREATE PROCEDURE obtenerUsuarios()
BEGIN
    SELECT idUsuario as ID, 
    nombre as name, 
    correo as email, 
    descripcion as role
    FROM Usuarios u JOIN Tipos_Usuario t ON u.idTipo = t.idTipo;
END $$
DELIMITER ;

-- Stored procedure para productos recomendados (mas vendidos)
DELIMITER $$
CREATE PROCEDURE productosRecomendados()
BEGIN
    SELECT p.idProducto AS ID, 
           p.nombre AS name, 
           p.precio AS price, 
           p.inventarioProducto AS stock,
           tc.descripcion AS category, 
           p.rutaImagen AS image
    FROM Productos p
    JOIN Contiene c ON p.idProducto = c.idProducto
    JOIN Tipos_Categorias tc ON p.idCategoria = tc.idCategoria
    GROUP BY p.idProducto
    ORDER BY SUM(c.cantidad) DESC;
END $$
DELIMITER ;

-- Stored procedure para ver productos por categoria
DELIMITER $$
CREATE PROCEDURE productosPorCategoria(
    IN cat VARCHAR(100)
)
BEGIN
    SELECT p.idProducto as ID, 
    p.nombre as name, 
    p.precio as price, 
    p.inventarioProducto as stock, 
    tc.descripcion as category, 
    p.rutaImagen as image
    FROM Productos p
    JOIN Tipos_Categorias tc ON p.idCategoria = tc.idCategoria
    WHERE tc.descripcion = cat;
END $$
DELIMITER ;

--Stored procedure para ver productos por ID
DELIMITER $$
CREATE PROCEDURE productoPorID(
    IN idProd INT
)
BEGIN
    SELECT p.idProducto AS ID, 
           p.nombre AS name, 
           p.precio AS price, 
           p.inventarioProducto AS stock,
           tc.descripcion AS category, 
           p.rutaImagen AS image
    FROM Productos p
    JOIN Tipos_Categorias tc ON p.idCategoria = tc.idCategoria
    WHERE p.idProducto = idProd;
END $$
DELIMITER ;

--Stored procedure para ver todos los productos
DELIMITER $$
CREATE PROCEDURE obtenerProductos()
BEGIN
    SELECT 
        Productos.idProducto AS ID, 
        Productos.nombre AS name, 
        Productos.precio AS price, 
        Productos.inventarioProducto AS stock, 
        Tipos_Categorias.descripcion AS category,
        Productos.rutaImagen AS image
    FROM Productos
    JOIN Tipos_Categorias ON Productos.idCategoria = Tipos_Categorias.idCategoria;
END $$
DELIMITER ;

--Stored Procedure para checar si la persona que quiere hacer una reseña si lo compro
DELIMITER $$
CREATE PROCEDURE aniadirResena(
    IN idUsuario INT,
    IN idProducto INT,
    IN calificacion INT,
    IN comentario VARCHAR(255)
)
BEGIN 
    DECLARE compra_existente INT DEFAULT 0;
    SELECT COUNT(*) INTO compra_existente FROM Contiene c JOIN Ventas co ON c.idCompra = co.idCompra
    WHERE co.idUsuario = idUsuario AND c.idProducto = idProducto;
    IF compra_existente = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se ha comprado el producto';
    ELSE
        INSERT INTO Resenas(idUsuario, idProducto, calificacion, comentario) VALUES(idUsuario, idProducto, calificacion, comentario);
    END IF;
END $$
DELIMITER ;

--Stored Procedure para hacer una compra
DELIMITER $$
CREATE PROCEDURE aniadirCompra(
    IN idU INT,
    IN dir TEXT,
    IN tipoEnvio INT
)
BEGIN
    if tipoEnvio = 1 THEN
        INSERT INTO Ventas(fecha, direccion, idUsuario, idEnvio, fecha_entrega) VALUES(CURDATE(), dir, idU, tipoEnvio, CURDATE() + INTERVAL 5 DAY);
    ELSEIF tipoEnvio = 2 THEN
        INSERT INTO Ventas(fecha, direccion, idUsuario, idEnvio, fecha_entrega) VALUES(CURDATE(), dir, idU, tipoEnvio, CURDATE() + INTERVAL 3 DAY);
    ELSEIF tipoEnvio = 3 THEN
        INSERT INTO Ventas(fecha, direccion, idUsuario, idEnvio, fecha_entrega) VALUES(CURDATE(), dir, idU, tipoEnvio, CURDATE() + INTERVAL 1 DAY);
    END IF;
END $$
DELIMITER ;

--Stored procedure para regresar la ultima compra
DELIMITER $$
CREATE PROCEDURE ultimaCompra(
    IN idU INT
)
BEGIN
    SELECT idCompra as ID
    FROM Ventas
    WHERE idUsuario = idU
    ORDER BY idCompra DESC
    LIMIT 1;
END $$
DELIMITER ;

--Stored Procedure para añadir contiene
DELIMITER $$
CREATE PROCEDURE aniadirContiene(
    IN idP INT,
    IN idC INT,
    IN cant INT
)
BEGIN
    DECLARE stock INT DEFAULT 0;
    select inventarioProducto into stock from Productos where idProducto = idP;
    IF stock < cant THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No hay suficiente stock';
    ELSE
        INSERT INTO Contiene(idProducto, idCompra, cantidad) VALUES(idP, idC, cant);
    END IF;
END $$



-- Procedimiento almacenado para cambiar el rol de un usuario
DELIMITER $$
CREATE PROCEDURE cambiarRol(
    IN p_idUsuario INT,
    IN p_idTipo INT
)
BEGIN
    UPDATE Usuarios SET idTipo = p_idTipo WHERE idUsuario = p_idUsuario;
END $$
DELIMITER ;

--Procedimiento almacenado para obtener las reseñas de un producto donde regrese el nombre del usuario y id del producto y usuario
DELIMITER $$
CREATE PROCEDURE obtenerResenas(
    IN p_idProducto INT
)
BEGIN
    SELECT r.idReseña as ID, 
    u.nombre as name, 
    r.calificacion as rating, 
    r.comentario as comment
    FROM Resenas r JOIN Usuarios u ON r.idUsuario = u.idUsuario
    WHERE r.idProducto = p_idProducto;
END $$
DELIMITER ;

--Stored procedure para obtener las ventas recientes de un usuario
DELIMITER $$
CREATE PROCEDURE obtenerVentasUsuario(
    IN p_idUsuario INT
)
BEGIN
    SELECT c.idCompra as ID, 
    c.fecha as date, 
    p.nombre as name, 
    p.precio as price,
    tc.descripcion as category,
    p.rutaImagen as image,
    tp.descripcion as status
    FROM Tipos_Status tp 
    JOIN Ventas c ON c.idStatus = tp.idStatus 
    JOIN Contiene co ON c.idCompra = co.idCompra
    JOIN Productos p ON co.idProducto = p.idProducto
    JOIN Tipos_Categorias tc ON p.idCategoria = tc.idCategoria
    WHERE c.idUsuario = p_idUsuario;
END $$
DELIMITER ;


--Stored procedure para ganancias totales
DELIMITER $$
CREATE PROCEDURE gananciasTotales()
BEGIN
    WITH tablaTotal1 AS(
    SELECT SUM(precio*cantidad) as total1
    FROM Productos prod JOIN Contiene cont ON prod.idProducto=cont.idProducto)
    , tablaTotal2 AS(
    SELECT SUM(precioProveedor * cantidad) as total2
    FROM Viene_De)
    SELECT total1 - total2 as total 
    FROM tablaTotal1 JOIN tablaTotal2;
END $$
DELIMITER ;

--Stored procedure para ingresos de cierto mes
DELIMITER $$
CREATE PROCEDURE ingresosMes(
    IN mes INT,
    IN anio INT
)
BEGIN
    WITH tablaTotal AS(
    SELECT precio*cantidad as total
    FROM Productos prod JOIN Contiene cont ON prod.idProducto=cont.idProducto
    JOIN Ventas comp ON comp.idCompra = cont.idCompra
    WHERE fecha LIKE CONCAT( CAST(anio AS CHAR) , '-', CAST(mes AS CHAR),'%'))
    SELECT SUM(total) as ingresosMes FROM tablaTotal;
END $$
DELIMITER ;

--Stored procedure para egresos de cierto mes
DELIMITER $$
CREATE PROCEDURE egresosMes(
    IN mes INT,
    IN anio INT
)
BEGIN
    WITH tablaTotal AS(
    SELECT precioProveedor * cantidad as total
    FROM Viene_De v JOIN Compras p ON p.idCompraProveedor = v.idCompraProveedor
    WHERE fecha LIKE CONCAT( CAST(anio AS CHAR) , '-', CAST(mes AS CHAR),'%'))
    SELECT SUM(total) as egresosMes FROM tablaTotal;
END $$
DELIMITER ;


--Stored procedures para 5 productos mas vendidos
DELIMITER $$
CREATE PROCEDURE masVendidos()
BEGIN
    SELECT nombre, SUM(cantidad) as cantidad
    FROM Contiene c JOIN Productos p ON c.idProducto = p.idProducto
    GROUP BY c.idProducto 
    ORDER BY cantidad DESC LIMIT 5;
END $$
DELIMITER ;

--Stored procedure para los proveedores regresando el porcentaje de compras totales
DELIMITER $$
CREATE PROCEDURE porcentajeProveedor()
BEGIN
    SELECT nombreProveedor, SUM(precioProveedor * cantidad) / (SELECT SUM(precioProveedor * cantidad) FROM Viene_De) as porcentaje
    FROM Proveedores p JOIN Compras pc ON p.idProveedor = pc.idProveedor
    JOIN Viene_De vd ON pc.idCompraProveedor = vd.idCompraProveedor GROUP BY p.idProveedor;
END $$
DELIMITER ;

--Total de compras por proveedor del ultimo mes
DELIMITER $$
CREATE PROCEDURE totalProveedorMes(
    IN mes INT,
    IN anio INT
)
BEGIN
    SELECT nombreProveedor, SUM(precioProveedor * cantidad) as total
    FROM Proveedores p JOIN Compras pc ON p.idProveedor = pc.idProveedor
    JOIN Viene_De vd ON pc.idCompraProveedor = vd.idCompraProveedor 
    WHERE fecha LIKE CONCAT( CAST(anio AS CHAR) , '-', CAST(mes AS CHAR),'%')
    GROUP BY p.idProveedor;
END $$
DELIMITER ;

--Stored procedure para los proveedores regresando el total de compras de todos los tiempos
DELIMITER $$
CREATE PROCEDURE totalProveedor()
BEGIN
    SELECT nombreProveedor, SUM(precioProveedor * cantidad) as total
    FROM Proveedores p JOIN Compras pc ON p.idProveedor = pc.idProveedor
    JOIN Viene_De vd ON pc.idCompraProveedor = vd.idCompraProveedor GROUP BY p.idProveedor;
END $$
DELIMITER ;

--Stored procedure para stock por producto
DELIMITER $$
CREATE PROCEDURE stockProducto()
BEGIN
    SELECT nombre, inventarioProducto as stock
    FROM Productos;
END $$
DELIMITER ;

DELIMITER ;

--Stored procedure para obtener las categorias
DELIMITER $$
CREATE PROCEDURE obtenerCategorias()
BEGIN
    SELECT idCategoria as ID, 
    descripcion as name
    FROM Tipos_Categorias;
END $$
DELIMITER ;

-- Stored procedure para obtener todas las ventas
DELIMITER $$
CREATE PROCEDURE obtenerVentas()
BEGIN
    SELECT v.idCompra as ID, 
    v.fecha as saleDate,
    v.fecha_entrega as deliveryDate,
    SUM(p.precio * c.cantidad) as total,
    v.direccion as address,
    u.nombre as name,
    tp.descripcion as status
    FROM Tipos_Status tp 
    JOIN Ventas v ON v.idStatus = tp.idStatus
    JOIN Contiene c ON v.idCompra = c.idCompra
    JOIN Productos p ON c.idProducto = p.idProducto
    JOIN Usuarios u ON v.idUsuario = u.idUsuario
    GROUP BY v.idCompra, v.fecha, v.fecha_entrega, v.direccion, u.nombre, tp.descripcion;
END $$
DELIMITER ;
-- Stored procedure para calcular el total incluyendo el descuento del cupón
DELIMITER $$
CREATE PROCEDURE calcularTotalConDescuento(
    IN idCompra INT
)
BEGIN
    DECLARE total DECIMAL(10,2);
    DECLARE descuento INT;
    DECLARE totalConDescuento DECIMAL(10,2);

    -- Calcular el total de la compra
    SELECT SUM(p.precio * c.cantidad) INTO total
    FROM Productos p
    JOIN Contiene c ON p.idProducto = c.idProducto
    WHERE c.idCompra = idCompra;

    -- Obtener el descuento del cupón
    SELECT cu.descuento INTO descuento
    FROM Ventas v
    JOIN Cupones cu ON v.codigoCupon = cu.codigoCupon
    WHERE v.idCompra = idCompra;

    -- Calcular el total con descuento
    SET totalConDescuento = total - (total * descuento / 100);

    -- Devolver el total con descuento
    SELECT totalConDescuento AS totalConDescuento;
END $$

DELIMITER ;

-- Obtener los productos de una venta
DELIMITER $$
CREATE PROCEDURE obtenerProductosVenta(
    IN idCompra INT
)
BEGIN
    SELECT p.idProducto as ID,
    p.nombre as name, 
    c.cantidad as quantity, 
    p.precio as price, 
    p.imagen as image,
    tc.descripcion as category
    FROM Productos p 
    JOIN Contiene c ON p.idProducto = c.idProducto
    JOIN Tipos_Categorias tc ON p.idCategoria = tc.idCategoria
    WHERE c.idCompra = idCompra;
END $$
DELIMITER ;

-- Procedimiento almacenado actualizar el estado de una venta
DELIMITER $$
CREATE PROCEDURE actualizarEstadoVenta(
    IN p_idCompra INT,
    IN p_idStatus INT
)
BEGIN
    UPDATE Ventas SET idStatus = p_idStatus WHERE idCompra = p_idCompra;
END $$
DELIMITER ;

-- Procedimiento para crear un producto
DELIMITER $$
CREATE PROCEDURE crearProducto(
    IN p_nombre VARCHAR(255),
    IN p_precio INT,
    IN p_inventario INT,
    IN p_idCategoria INT,
    IN p_rutaImagen VARCHAR(100)
)
BEGIN
    INSERT INTO Productos(nombre, precio, inventarioProducto, idCategoria, rutaImagen) VALUES(p_nombre, p_precio, p_inventario, p_idCategoria, p_rutaImagen);
END $$
DELIMITER ;

-- Procedimiento para eliminar a un usuario si no tiene compras
DELIMITER $$
CREATE PROCEDURE eliminarUsuario(
    IN p_idUsuario INT
)
BEGIN
    DECLARE compras INT;
    SELECT COUNT(*) INTO compras FROM Ventas WHERE idUsuario = p_idUsuario;
    IF compras = 0 THEN
        DELETE FROM Usuarios WHERE idUsuario = p_idUsuario;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El usuario tiene compras';
    END IF;
END $$
DELIMITER ;

-- Procedimiento para eliminar un producto si no tiene compras
DELIMITER $$
CREATE PROCEDURE eliminarProducto(
    IN p_idProducto INT
)
BEGIN
    DECLARE compras INT;
    SELECT COUNT(*) INTO compras FROM Contiene WHERE idProducto = p_idProducto;
    IF compras = 0 THEN
        DELETE FROM Productos WHERE idProducto = p_idProducto;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El producto tiene compras';
    END IF;
END $$