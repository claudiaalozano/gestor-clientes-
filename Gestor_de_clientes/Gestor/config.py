import sys
DATABASE_PATH = './Gestor_de_clientes/clientes.csv.'

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = './Gestor_de_Clientes/tests/clientes_test.csv'

