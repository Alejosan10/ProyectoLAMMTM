# coding=utf-8

from faker import Faker
import psycopg2

# Configuración de conexión a la base de datos
conn = psycopg2.connect(
    dbname='BankDBMgmt',
    user='LAMMTM',
    password='LAMMTMproy@',
    host='localhost',
    port='5433'
)
cur = conn.cursor()

# Inicializar Faker
fake = Faker()

# Generar datos para la tabla Clientes
def generate_clientes(n):
    clientes = []
    for _ in range(n):
        nombre = fake.name()
        direccion = fake.address()
        telefono = fake.phone_number()
        correo_electronico = fake.email()
        fecha_registro = fake.date_this_decade()
        clientes.append((nombre, direccion, telefono, correo_electronico, fecha_registro))
    return clientes

# Generar datos para la tabla Cuentas
def generate_cuentas(n, clientes_ids):
    cuentas = []
    for _ in range(n):
        id_cliente = fake.random_element(clientes_ids)
        tipo_cuenta = fake.random_element(['Ahorro', 'Corriente'])
        saldo = round(fake.random_number(digits=5), 2)
        fecha_apertura = fake.date_this_decade()
        estado = fake.random_element(['Activa', 'Inactiva'])
        cuentas.append((id_cliente, tipo_cuenta, saldo, fecha_apertura, estado))
    return cuentas

# Generar datos para la tabla Transacciones
def generate_transacciones(n, cuentas_ids):
    transacciones = []
    for _ in range(n):
        id_cuenta = fake.random_element(cuentas_ids)
        tipo_transaccion = fake.random_element(['Deposito', 'Retiro', 'Transferencia'])
        monto = round(fake.random_number(digits=4), 2)
        fecha_transaccion = fake.date_this_decade()
        descripcion = fake.text(max_nb_chars=200)
        transacciones.append((id_cuenta, tipo_transaccion, monto, fecha_transaccion, descripcion))
    return transacciones

# Generar datos para la tabla Prestamos
def generate_prestamos(n, clientes_ids):
    prestamos = []
    for _ in range(n):
        id_cliente = fake.random_element(clientes_ids)
        monto_prestamo = round(fake.random_number(digits=5), 2)
        tasa_interes = round(fake.random_number(digits=2), 2)
        fecha_aprobacion = fake.date_this_decade()
        estado = fake.random_element(['Aprobado', 'Pendiente', 'Rechazado'])
        prestamos.append((id_cliente, monto_prestamo, tasa_interes, fecha_aprobacion, estado))
    return prestamos

# Generar datos para la tabla PagosPrestamos
def generate_pagos_prestamos(n, prestamos_ids):
    pagos_prestamos = []
    for _ in range(n):
        id_prestamo = fake.random_element(prestamos_ids)
        monto_pago = round(fake.random_number(digits=4), 2)
        fecha_pago = fake.date_this_decade()
        estado_pago = fake.random_element(['Completado', 'Pendiente'])
        pagos_prestamos.append((id_prestamo, monto_pago, fecha_pago, estado_pago))
    return pagos_prestamos

# Generar datos para la tabla Tarjetas
def generate_tarjetas(n, clientes_ids):
    tarjetas = []
    for _ in range(n):
        id_cliente = fake.random_element(clientes_ids)
        tipo_tarjeta = fake.random_element(['Credito', 'Debito'])
        numero_tarjeta = fake.credit_card_number()
        fecha_emision = fake.date_this_decade()
        fecha_vencimiento = fake.future_date(end_date="+5y", tzinfo=None)
        limite_credito = round(fake.random_number(digits=5), 2)
        tarjetas.append((id_cliente, tipo_tarjeta, numero_tarjeta, fecha_emision, fecha_vencimiento, limite_credito))
    return tarjetas

# Generar datos para la tabla HistorialCrediticio
def generate_historial_crediticio(n, clientes_ids):
    historial = []
    for _ in range(n):
        id_cliente = fake.random_element(clientes_ids)
        calificacion_crediticia = fake.random_element(['Excelente', 'Buena', 'Regular', 'Mala'])
        fecha_revision = fake.date_this_decade()
        detalles = fake.text(max_nb_chars=200)
        historial.append((id_cliente, calificacion_crediticia, fecha_revision, detalles))
    return historial

# Generar datos para la tabla Inversiones
def generate_inversiones(n, clientes_ids):
    inversiones = []
    for _ in range(n):
        id_cliente = fake.random_element(clientes_ids)
        tipo_inversion = fake.random_element(['Bonos', 'Acciones', 'Fondos Mutuos'])
        monto_inversion = round(fake.random_number(digits=5), 2)
        fecha_inversion = fake.date_this_decade()
        estado_inversion = fake.random_element(['Activa', 'Cerrada'])
        rendimiento = round(fake.random_number(digits=2), 2)
        inversiones.append((id_cliente, tipo_inversion, monto_inversion, fecha_inversion, estado_inversion, rendimiento))
    return inversiones

# Generar datos para la tabla PagosServicios
def generate_pagos_servicios(n, clientes_ids):
    pagos_servicios = []
    for _ in range(n):
        id_cliente = fake.random_element(clientes_ids)
        tipo_servicio = fake.random_element(['Electricidad', 'Agua', 'Internet', 'Gas'])
        monto = round(fake.random_number(digits=4), 2)
        fecha_pago = fake.date_this_decade()
        estado_pago = fake.random_element(['Pagado', 'Pendiente'])
        pagos_servicios.append((id_cliente, tipo_servicio, monto, fecha_pago, estado_pago))
    return pagos_servicios

# Insertar datos en las tablas
def insert_data():
    # Insertar datos en Clientes
    clientes = generate_clientes(100)
    cur.executemany("INSERT INTO Clientes (nombre, direccion, telefono, correo_electronico, fecha_registro) VALUES (%s, %s, %s, %s, %s) RETURNING id_cliente", clientes)
    clientes_ids = [row[0] for row in cur.fetchall()]

    # Insertar datos en Cuentas
    cuentas = generate_cuentas(200, clientes_ids)
    cur.executemany("INSERT INTO Cuentas (id_cliente, tipo_cuenta, saldo, fecha_apertura, estado) VALUES (%s, %s, %s, %s, %s) RETURNING id_cuenta", cuentas)
    cuentas_ids = [row[0] for row in cur.fetchall()]

    # Insertar datos en Transacciones
    transacciones = generate_transacciones(500, cuentas_ids)
    cur.executemany("INSERT INTO Transacciones (id_cuenta, tipo_transaccion, monto, fecha_transaccion, descripcion) VALUES (%s, %s, %s, %s, %s)", transacciones)

    # Insertar datos en Prestamos
    prestamos = generate_prestamos(100, clientes_ids)
    cur.executemany("INSERT INTO Prestamos (id_cliente, monto_prestamo, tasa_interes, fecha_aprobacion, estado) VALUES (%s, %s, %s, %s, %s) RETURNING id_prestamo", prestamos)
    prestamos_ids = [row[0] for row in cur.fetchall()]

    # Insertar datos en PagosPrestamos
    pagos_prestamos = generate_pagos_prestamos(300, prestamos_ids)
    cur.executemany("INSERT INTO PagosPrestamos (id_prestamo, monto_pago, fecha_pago, estado_pago) VALUES (%s, %s, %s, %s)", pagos_prestamos)

    # Insertar datos en Tarjetas
    tarjetas = generate_tarjetas(200, clientes_ids)
    cur.executemany("INSERT INTO Tarjetas (id_cliente, tipo_tarjeta, numero_tarjeta, fecha_emision, fecha_vencimiento, limite_credito) VALUES (%s, %s, %s, %s, %s, %s)", tarjetas)

    # Insertar datos en HistorialCrediticio
    historial = generate_historial_crediticio(100, clientes_ids)
    cur.executemany("INSERT INTO HistorialCrediticio (id_cliente, calificacion_crediticia, fecha_revision, detalles) VALUES (%s, %s, %s, %s)", historial)

    # Insertar datos en Inversiones
    inversiones = generate_inversiones(150, clientes_ids)
    cur.executemany("INSERT INTO Inversiones (id_cliente, tipo_inversion, monto_inversion, fecha_inversion, estado_inversion, rendimiento) VALUES (%s, %s, %s, %s, %s, %s)", inversiones)

    # Insertar datos en PagosServicios
    pagos_servicios = generate_pagos_servicios(400, clientes_ids)
    cur.executemany("INSERT INTO PagosServicios (id_cliente, tipo_servicio, monto, fecha_pago, estado_pago) VALUES (%s, %s, %s, %s, %s)", pagos_servicios)

    # Guardar cambios y cerrar la conexión
    conn.commit()
    cur.close()
    conn.close()

if _name_ == '_main_':
    insert_data()
