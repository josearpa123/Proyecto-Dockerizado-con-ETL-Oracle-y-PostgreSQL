import psycopg2
import random

# Parámetros de conexión a la base de datos
db_params = {
    'host': '192.168.16.2',  # Nombre del servicio de la base de datos
    'port': 5433,                # Puerto del contenedor mapeado
    'dbname': 'postgres',        # Nombre de la base de datos
    'user': 'user',              # Usuario de la base de datos
    'password': 'password'       # Contraseña de la base de datos
}

# Conectar a la base de datos
try:
    conn = psycopg2.connect(**db_params)
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
    exit()

cursor = conn.cursor()

# Crear una tabla para almacenar los números aleatorios
cursor.execute('''
CREATE TABLE IF NOT EXISTS numeros_aleatorios (
    id SERIAL PRIMARY KEY,
    numero INTEGER NOT NULL
);
''')
conn.commit()

# Generar e insertar números aleatorios en la tabla
def generar_numeros_aleatorios(n):
    for _ in range(n):
        numero = random.randint(0, 100)
        cursor.execute('INSERT INTO numeros_aleatorios (numero) VALUES (%s)', (numero,))
    conn.commit()

# Generar 10 números aleatorios
generar_numeros_aleatorios(10)

# Cerrar la conexión a la base de datos
cursor.close()
conn.close()
