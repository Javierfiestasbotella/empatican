import psycopg2
from psycopg2 import sql

def create_connection():
    """
    Establece la conexión con la base de datos PostgreSQL.
    """
    try:
        conn = psycopg2.connect(
            dbname="clientes_db",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
            options="-c client_encoding=UTF8"
        )
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Error: {e}")
        return None

def initialize_database():
    """
    Crea las tablas necesarias en la base de datos si no existen.
    """
    conn = create_connection()
    if conn is None:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conn.cursor()

    # Crear la tabla Clientes_empatican
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes_empatican (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        telefono VARCHAR(20),
        email VARCHAR(100),
        direccion TEXT,
        fecha_registro DATE DEFAULT CURRENT_DATE
    );
    ''')

    # Crear la tabla Perros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS perros (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        raza VARCHAR(50),
        edad INTEGER,
        cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
        notas TEXT
    );
    ''')

    # Crear la tabla Sesiones
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sesiones (
        id SERIAL PRIMARY KEY,
        perro_id INTEGER REFERENCES perros(id) ON DELETE CASCADE,
        fecha DATE NOT NULL,
        descripcion TEXT,
        duracion INTEGER,
        costo DECIMAL(10, 2)
    );
    ''')

    # Crear la tabla Seminarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seminarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        fecha DATE NOT NULL,
        costo DECIMAL(10, 2)
    );
    ''')

    # Crear la tabla Inscripciones a Seminarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inscripciones_seminarios (
        id SERIAL PRIMARY KEY,
        cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
        seminario_id INTEGER REFERENCES seminarios(id) ON DELETE CASCADE,
        fecha_inscripcion DATE NOT NULL
    );
    ''')

    # Crear la tabla Pagos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagos (
        id SERIAL PRIMARY KEY,
        cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
        fecha DATE NOT NULL,
        monto DECIMAL(10, 2),
        metodo_pago VARCHAR(50),
        concepto TEXT,
        nota TEXT
    );
    ''')

    conn.commit()
    cursor.close()
    conn.close()

    print("Tablas creadas correctamente.")

if __name__ == "__main__":
    initialize_database()
