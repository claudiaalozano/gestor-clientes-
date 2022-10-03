import copy
import unittest
import database as db 

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Cliente.lista =  [
 db.Cliente('15J', 'Marta', 'Pérez'),
 db.Cliente('48H', 'Manolo', 'López'),
 db.Cliente('28Z', 'Ana', 'García')
 ]

    def test_buscar_cliente(self):
        cliente_existente = db.Cliente.buscar("15J")
        cliente_no_existente = db.Cliente.buscar("99X")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_no_existente)
    
    def test_crear_cliente(self):
        nuevo_cliente = db.Cliente.crear("39X" , "Héctor" , "Costa")
        self.assertEqual(len(db.Cliente.lista), 4)
        self.assertEqual(nuevo_cliente.dni, "39X")
        self.assertEqual(nuevo_cliente.nombre, "Hector")
        self.assertEqual(nuevo_cliente.apellido, "Costa")

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Cliente.buscar("28Z"))
        cliente_modificado = db.Cliente.modificar("28Z" , "Marina" , "Pérez")
        self.assertEqual(cliente_a_modificar.nombre, "Ana")
        self.assertEqual(cliente_modificado.nombre, "Marina")

    def test_borrar_cliente(self):
        cliente_borrado= db.Cliente.borrar("48H")
        cliente_rebuscado = db.Cliente.buscar("48H")
        self.assertEqual(cliente_borrado, cliente_rebuscado)

if __name__ == "__main__":
    unittest.main()
    