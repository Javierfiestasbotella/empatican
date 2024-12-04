import unittest
from models import Cliente, Perro, Sesion, Seminario, Pago
from db_setup import create_connection

class TestDatabaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Configura una conexión de prueba antes de ejecutar todas las pruebas.
        """
        cls.connection = create_connection()
        cls.cursor = cls.connection.cursor()

    @classmethod
    def tearDownClass(cls):
        """
        Cierra la conexión después de ejecutar todas las pruebas.
        """
        cls.cursor.close()
        cls.connection.close()

    def test_crear_cliente(self):
        cliente = Cliente(nombre="Test User", telefono="123456789", email="test@example.com", direccion="123 Test St")
        cliente.save()
        self.cursor.execute("SELECT nombre FROM clientes_empatican WHERE nombre = %s", (cliente.nombre,))
        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], "Test User")

    def test_crear_perro(self):
        cliente = Cliente(nombre="Owner Test", telefono="987654321", email="owner@example.com", direccion="321 Test Ave")
        cliente.save()
        
        perro = Perro(nombre="Firulais", raza="Labrador", edad=5, cliente_id=cliente.id, notas="Prueba de perro", foto="")
        perro.save()
        self.cursor.execute("SELECT nombre FROM perros WHERE nombre = %s", (perro.nombre,))
        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], "Firulais")

    def test_crear_seminario(self):
        seminario = Seminario(nombre="Test Seminario", descripcion="Descripción de prueba", fecha="2024-11-05", costo=50.0)
        seminario.save()
        self.cursor.execute("SELECT nombre FROM seminarios WHERE nombre = %s", (seminario.nombre,))
        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], "Test Seminario")

    def test_crear_pago(self):
        cliente = Cliente(nombre="Payer Test", telefono="111222333", email="payer@example.com", direccion="789 Test Blvd")
        cliente.save()
        
        pago = Pago(cliente_id=cliente.id, fecha="2024-11-04", monto=100.0, metodo_pago="Tarjeta", concepto="Test Payment", nota="Pago de prueba")
        pago.save()
        self.cursor.execute("SELECT monto FROM pagos WHERE cliente_id = %s", (cliente.id,))
        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], 100.0)
def test_crear_pago(self):
    # Creamos el cliente y lo guardamos
    cliente = Cliente(nombre="Payer Test", telefono="111222333", email="payer@example.com", direccion="789 Test Blvd")
    cliente.save()
    
    # Recuperamos el cliente recién creado para obtener su id
    self.cursor.execute("SELECT id FROM clientes_empatican WHERE nombre = %s", (cliente.nombre,))
    cliente_id = self.cursor.fetchone()[0]
    
    # Creamos el pago con el id del cliente recuperado
    pago = Pago(cliente_id=cliente_id, fecha="2024-11-04", monto=100.0, metodo_pago="Tarjeta", concepto="Test Payment", nota="Pago de prueba")
    pago.save()
    
    # Verificamos si el pago se guardó correctamente
    self.cursor.execute("SELECT monto FROM pagos WHERE cliente_id = %s", (cliente_id,))
    resultado = self.cursor.fetchone()
    self.assertIsNotNone(resultado)
    self.assertEqual(resultado[0], 100.0)


if __name__ == "__main__":
    unittest.main()
