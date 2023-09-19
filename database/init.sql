-- Seleccionar la base de datos en la que se ejecutarán las consultas
USE practica01;

-- Crear una tabla llamada "usuarios"
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar algunos registros iniciales
INSERT INTO usuarios (nombre) VALUES
  ('Juan Perez'),
  ('Maria Gonzalez'),
  ('Carlos Rodriguez');
