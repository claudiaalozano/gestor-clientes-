class Cliente:

    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido =apellido
    
    def __str__(self):
        return f"({self.dni}), {self.nombre}, {self.apellido}"

    lista = []

    @staticmethod
    def buscar(dni):
        for cliente in Cliente.lista:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Cliente.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for i, cliente in enumerate(Cliente.lista):
            if cliente.dni == dni:
                Cliente.lista[i].nombre = nombre
                Cliente.lista[i].apellido = apellido
                return Cliente.lista[i]
    
    @staticmethod
    def borrar(dni):
        for i, cliente in enumerate(Cliente.lista):
            if cliente.dni == dni:
                cliente = Cliente.lista.pop(i)
                return cliente
                
