import psycopg2
from db_setup import create_connection

# Clase Cliente
class Cliente:
    def __init__(self, nombre, telefono, email, direccion, id=None):
        self.id = id  # El id es opcional y solo se asigna cuando ya existe
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def save(self):
        """
        Guarda el cliente en la base de datos (tabla clientes_empatican).
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes_empatican (nombre, telefono, email, direccion) VALUES (%s, %s, %s, %s)",
            (self.nombre, self.telefono, self.email, self.direccion)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all():
        """
        Recupera todos los clientes de la base de datos (tabla clientes_empatican) y los convierte en objetos Cliente.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, telefono, email, direccion FROM clientes_empatican")
        rows = cursor.fetchall()

        clientes = []
        for row in rows:
            cliente = Cliente(id=row[0], nombre=row[1], telefono=row[2], email=row[3], direccion=row[4])
            clientes.append(cliente)

        cursor.close()
        conn.close()

        return clientes

    @staticmethod
    def get_by_id(cliente_id):
        """
        Recupera un cliente por su ID.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, telefono, email, direccion FROM clientes_empatican WHERE id = %s", (cliente_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return Cliente(id=row[0], nombre=row[1], telefono=row[2], email=row[3], direccion=row[4])
        return None

# Clase Perro
class Perro:
    def __init__(self, nombre, raza, edad, cliente_id, notas="", foto="", id=None):
        self.id = id  # Ahora 'id' es opcional
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.cliente_id = cliente_id
        self.notas = notas
        self.foto = foto

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO perros (nombre, raza, edad, cliente_id, notas, foto) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.nombre, self.raza, self.edad, self.cliente_id, self.notas, self.foto)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_cliente(cliente_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, raza, edad, cliente_id, notas, foto FROM perros WHERE cliente_id = %s", (cliente_id,))
        rows = cursor.fetchall()
        
        perros = []
        for row in rows:
            # CORRECCIÓN: Ahora obtenemos también el campo 'foto' en row[6]
            # Comentario de depuración para ver los resultados obtenidos desde la base de datos
            print(row)  # Depuración para ver los resultados

            # Asignamos correctamente todos los campos, incluyendo 'foto' (row[6])
            perro = Perro(id=row[0], nombre=row[1], raza=row[2], edad=row[3], cliente_id=row[4], notas=row[5], foto=row[6])
            perros.append(perro)
        
        cursor.close()
        conn.close()
        
        return perros


# Nueva Clase Seminario
class Seminario:
    def __init__(self, nombre, descripcion, fecha, costo, cliente_id=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.costo = costo
        self.cliente_id = cliente_id  # Agregar cliente_id para asociar el seminario con un cliente

    def save(self):
        """
        Guarda el seminario en la base de datos.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO seminarios (nombre, descripcion, fecha, costo, cliente_id) VALUES (%s, %s, %s, %s, %s)",
            (self.nombre, self.descripcion, self.fecha, self.costo, self.cliente_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all():
        """
        Recupera todos los seminarios de la base de datos.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM seminarios")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_by_cliente(cliente_id):
        """
        Recupera todos los seminarios en los que se ha inscrito un cliente específico.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, descripcion, fecha, costo FROM seminarios WHERE cliente_id = %s", (cliente_id,))
        rows = cursor.fetchall()
        
        seminarios = []
        for row in rows:
            seminario = Seminario(nombre=row[0], descripcion=row[1], fecha=row[2], costo=row[3], cliente_id=cliente_id)
            seminarios.append(seminario)
        
        cursor.close()
        conn.close()
        
        return seminarios

# Nueva clase Pago
class Pago:
    def __init__(self, cliente_id, fecha, monto, metodo_pago, concepto, nota=""):
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.concepto = concepto
        self.nota = nota

    def save(self):
        """
        Guarda el pago en la base de datos.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pagos (cliente_id, fecha, monto, metodo_pago, concepto, nota) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.cliente_id, self.fecha, self.monto, self.metodo_pago, self.concepto, self.nota)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_cliente(cliente_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT fecha, monto, metodo_pago, concepto FROM pagos WHERE cliente_id = %s", (cliente_id,))
        rows = cursor.fetchall()
        
        pagos = []
        for row in rows:
            pago = Pago(cliente_id=cliente_id, fecha=row[0], monto=row[1], metodo_pago=row[2], concepto=row[3])
            pagos.append(pago)
        
        cursor.close()
        conn.close()
        
        return pagos
    
class Sesion:
    def __init__(self, perro_id, fecha, duracion, descripcion, costo):
        self.perro_id = perro_id  # Cambiado a perro_id en lugar de cliente_id
        self.fecha = fecha
        self.duracion = duracion
        self.descripcion = descripcion
        self.costo = costo  # Asegúrate de que este campo esté incluido

    def save(self):
        """Guardar la sesión en la base de datos."""
        conn = create_connection()
        cursor = conn.cursor()

        # Asegúrate de que estás insertando el costo junto con los demás campos
        cursor.execute(
            "INSERT INTO sesiones (perro_id, fecha, duracion, descripcion, costo) VALUES (%s, %s, %s, %s, %s)",
            (self.perro_id, self.fecha, self.duracion, self.descripcion, self.costo)
        )

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_perro(perro_id):
        conn = create_connection()
        cursor = conn.cursor()
        query = """
        SELECT fecha, descripcion, duracion, costo
        FROM sesiones
        WHERE perro_id = %s
        """
        cursor.execute(query, (perro_id,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        sesiones = []
        for row in results:
            sesiones.append({
                'fecha': row[0],
                'descripcion': row[1],
                'duracion': row[2],
                'costo': row[3]
            })
        return sesiones