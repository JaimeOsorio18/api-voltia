-- SQLite
-- Obtener todos los equipos:

SELECT * FROM api_equipo;

-- Obtener los mantenimientos realizados en un equipo específico:

SELECT m.*
FROM api_mantenimiento m
JOIN api_equipo e ON m.equipo_id = e.equipo_id
WHERE e.nombre = 'Generador';

-- Obtener las lecturas de un equipo en un rango de fechas:

SELECT *
FROM api_lectura
WHERE equipo_id = 1
AND fecha BETWEEN '2022-01-01' AND '2022-12-31';

-- Obtener los equipos y sus mantenimientos correspondientes:

SELECT e.*, m.fecha, m.descripcion
FROM api_equipo e
LEFT JOIN api_mantenimiento m ON e.equipo_id = m.equipo_id;

-- Obtener los equipos con más de 2 lecturas registradas: 

SELECT e.*
FROM api_equipo e
JOIN api_lectura l ON e.equipo_id = l.equipo_id
GROUP BY e.equipo_id
HAVING COUNT(l.equipo_id) > 2;


