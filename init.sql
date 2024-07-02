-- Tabla Clientes
CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dirección VARCHAR(255) NOT NULL,
    teléfono VARCHAR(20) NOT NULL,
    correo_electrónico VARCHAR(100) NOT NULL,
    fecha_registro DATE NOT NULL
);

-- Tabla Cuentas
CREATE TABLE Cuentas (
    id_cuenta SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES Clientes(id_cliente),
    tipo_cuenta VARCHAR(50) NOT NULL,
    saldo DECIMAL(15, 2) NOT NULL,
    fecha_apertura DATE NOT NULL,
    estado VARCHAR(50) NOT NULL
);

-- Tabla Transacciones
CREATE TABLE Transacciones (
    id_transacción SERIAL PRIMARY KEY,
    id_cuenta INT REFERENCES Cuentas(id_cuenta),
    tipo_transacción VARCHAR(50) NOT NULL,
    monto DECIMAL(15, 2) NOT NULL,
    fecha_transacción TIMESTAMP NOT NULL,
    descripción TEXT
);

-- Tabla Préstamos
CREATE TABLE Préstamos (
    id_préstamo SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES Clientes(id_cliente),
    monto_préstamo DECIMAL(15, 2) NOT NULL,
    tasa_interés DECIMAL(5, 2) NOT NULL,
    fecha_aprobación DATE NOT NULL,
    estado VARCHAR(50) NOT NULL
);

-- Tabla PagosPréstamos
CREATE TABLE PagosPréstamos (
    id_pago SERIAL PRIMARY KEY,
    id_préstamo INT REFERENCES Préstamos(id_préstamo),
    monto_pago DECIMAL(15, 2) NOT NULL,
    fecha_pago DATE NOT NULL,
    estado_pago VARCHAR(50) NOT NULL
);

-- Tabla Empleados
CREATE TABLE Empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(50) NOT NULL,
    teléfono VARCHAR(20) NOT NULL,
    correo_electrónico VARCHAR(100) NOT NULL,
    fecha_contratación DATE NOT NULL
);

-- Tabla Tarjetas
CREATE TABLE Tarjetas (
    id_tarjeta SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES Clientes(id_cliente),
    tipo_tarjeta VARCHAR(50) NOT NULL,
    número_tarjeta VARCHAR(16) UNIQUE NOT NULL,
    fecha_emisión DATE NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    límite_credito DECIMAL(15, 2) NOT NULL
);

-- Tabla HistorialCrediticio
CREATE TABLE HistorialCrediticio (
    id_historial SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES Clientes(id_cliente),
    calificación_crediticia VARCHAR(50) NOT NULL,
    fecha_revisión DATE NOT NULL,
    detalles TEXT
);

-- Tabla Inversiones
CREATE TABLE Inversiones (
    id_inversión SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES Clientes(id_cliente),
    tipo_inversión VARCHAR(50) NOT NULL,
    monto_inversión DECIMAL(15, 2) NOT NULL,
    fecha_inversión DATE NOT NULL,
    estado_inversión VARCHAR(50) NOT NULL,
    rendimiento DECIMAL(5, 2) NOT NULL
);

-- Tabla PagosServicios
CREATE TABLE PagosServicios (
    id_pago_servicio SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES Clientes(id_cliente),
    tipo_servicio VARCHAR(50) NOT NULL,
    monto DECIMAL(15, 2) NOT NULL,
    fecha_pago DATE NOT NULL,
    estado_pago VARCHAR(50) NOT NULL
);

-----------------------------------------------------

-- Creación de roles y usuarios
CREATE ROLE rol_lectura;
CREATE ROLE rol_dba;

CREATE USER usr_empleado WITH PASSWORD 'Empleado3TMA';
GRANT rol_lectura TO usr_empleado;

CREATE USER usr_dba WITH PASSWORD 'Admin3AMT';
GRANT rol_dba TO usr_dba;

-----------------------------------------------------

-- Asignación de permisos
GRANT SELECT ON TABLE Clientes TO rol_lectura;
GRANT SELECT ON TABLE Cuentas TO rol_lectura;
GRANT SELECT ON TABLE Transacciones TO rol_lectura;
GRANT SELECT ON TABLE Tarjetas TO rol_lectura;
GRANT SELECT ON TABLE HistorialCrediticio TO rol_lectura;
GRANT SELECT ON TABLE Inversiones TO rol_lectura;
GRANT SELECT ON TABLE PagosServicios TO rol_lectura;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rol_dba;