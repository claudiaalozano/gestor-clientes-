import csv
import config

class Clientes:

    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido =apellido
    
    def __str__(self):
        return f"({self.dni}), {self.nombre}, {self.apellido}"

class Cliente:
    lista = []
    with open(config.DATABASE_PATH, newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dni, nombre, apellido in reader:
            cliente = Clientes(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Cliente.lista:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Cliente.lista.append(cliente)
        Cliente.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for i, cliente in enumerate(Cliente.lista):
            if cliente.dni == dni:
                Cliente.lista[i].nombre = nombre
                Cliente.lista[i].apellido = apellido
                Cliente.guardar()
                return Cliente.lista[i]
    
    @staticmethod
    def borrar(dni):
        for i, cliente in enumerate(Cliente.lista):
            if cliente.dni == dni:
                cliente = Cliente.lista.pop(i)
                Cliente.guardar()
                return cliente

    
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero: 
            writer = csv.writer(fichero, delimiter=";")
            for c in Cliente.lista:
                writer.writerow((c.dni, c.nombre, c.apellido))
                
