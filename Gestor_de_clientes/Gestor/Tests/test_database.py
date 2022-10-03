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