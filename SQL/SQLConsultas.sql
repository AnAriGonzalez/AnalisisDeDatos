CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;
 
-- Crear tabla estudiantes
CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
) ENGINE=InnoDB;
 
-- Crear tabla libros
CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100),
    disponible BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;
 
-- Crear tabla prestamos
CREATE TABLE prestamos (
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_libro INT NOT NULL,
    fecha_prestamo DATE NOT NULL DEFAULT (CURRENT_DATE),
    fecha_devolucion DATE,
    CONSTRAINT fk_estudiante FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    CONSTRAINT fk_libro FOREIGN KEY (id_libro) REFERENCES libros(id_libro),
    CONSTRAINT chk_fechas CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo)
) ENGINE=InnoDB;
-- CREACIÓN DE UNA BASE DATOS
CREATE DATABASE Libreria;
USE Libreria;
-- TABLA DE ESTUDIANTES
CREATE TABLE estudiantes (
id_estudiantes INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL
);
-- TABLA LIBROS
CREATE TABLE libros (
id_libro INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(100) NOT NULL,
autor VARCHAR(100) NOT NULL,  
disponible boolean default true
);
-- Tabla préstamos
CREATE TABLE prestamos (
id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
id_estudiante INT NOT NULL, -- Definición del campo
id_libro INT NOT NULL, -- Definición del campo
fecha_prestamo DATE NOT NULL DEFAULT (CURRENT_DATE),
fecha_devolucion DATE,
CONSTRAINT fk_estudiante FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiantes),
CONSTRAINT fk_libros foreign key(id_libro) references libros(id_libro),
CONSTRAINT chk_fechas CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo)
);
USE biblioteca; -- Seleccionar la base de datos biblioteca
 
-- Insertar registros en la tabla estudiante
INSERT INTO estudiantes (nombre, email) VALUES
('Ana Torres', 'ana.torres@gmail.com'),
('Luis Pérez', 'luis.perez@outlook.com'),
('Marta Silva', 'marta.silva@gmail.com'),
('Diego López', 'diego.lopez@yahoo.com'),
('Rosa Díaz', 'rosa.diaz@gmail.com'),
('Carlos Mora', 'carlos.mora@usf.edu'),
('Elena Ruiz', 'elena.ruiz@gmail.com');
 
-- Insertar registros en la tabla libros
INSERT INTO libros (titulo, autor, disponible) VALUES
('Cien años de soledad', 'Gabriel García Márquez', TRUE),
('El principito', 'Antoine de Saint-Exupéry', TRUE),
('1984', 'George Orwell', TRUE),
('Don Quijote de la Mancha', 'Miguel de Cervantes', TRUE),
('La Odisea', 'Homero', TRUE),
('Crónica de una muerte anunciada', 'Gabriel García Márquez', TRUE),
('El señor de los anillos', 'J.R.R. Tolkien', TRUE);
 
-- Insertar datos en la tabla préstamo
INSERT INTO prestamos (id_estudiante, id_libro, fecha_prestamo, fecha_devolucion) VALUES
(1, 1, '2025-07-01', '2025-07-10'),
(2, 2, '2025-07-02', NULL),
(3, 3, '2025-07-03', '2025-07-15'),
(1, 4, '2025-07-05', '2025-07-12'),
(4, 5, '2025-07-06', NULL),
(5, 6, '2025-07-07', '2025-07-18'),
(6, 1, '2025-07-08', NULL),
(2, 3, '2025-07-09', '2025-07-20'),
(3, 2, '2025-07-10', '2025-07-15'),
(7, 7, '2025-07-11', NULL);


USE biblioteca; -- Seleccionar la base de datos biblioteca
-- Actualizar datos de estudiante
UPDATE estudiantes
SET email = 'marta.silva.nuevo@gmail.com'
WHERE id_estudiante = 3;
 
-- Actualizar datos del libro
UPDATE libros
SET disponible = FALSE
WHERE id_libro = 2;
 
-- Actualizar fecha de devolución
UPDATE prestamos
SET fecha_devolucion = '2025-07-16'
WHERE id_prestamo = 2;
 
-- Eliminar un préstamo
DELETE FROM prestamos
WHERE id_prestamo = 5;
 
-- Eliminar un estudiante (solo si no tiene préstamos)
DELETE FROM estudiantes
WHERE id_estudiante = 7;
 
-- Eliminar un libro
DELETE FROM libros
WHERE id_libro = 7;


