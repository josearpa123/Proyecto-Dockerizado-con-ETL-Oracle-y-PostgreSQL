import psycopg2
import os
from time import sleep

# Parámetros de conexión desde variables de entorno
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'postgres')
DATABASE_USER = os.environ.get('DATABASE_USER', 'user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'password')

# Función para conectar a la base de datos
def connect_to_db():
    connection = None
    while connection is None:
        try:
            connection = psycopg2.connect(
                host=DATABASE_HOST,
                dbname=DATABASE_NAME,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD
            )
            print("Conectado a la base de datos.")
        except Exception as e:
            print(f"Error al conectar: {e}")
            sleep(5)
    return connection

# Función para consultar datos
def query_data():
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        # Consulta de datos
        cursor.execute("SELECT * FROM empleados")
        rows = cursor.fetchall()
        
        print("Datos de empleados:")
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error al consultar datos: {e}")
    finally:
        cursor.close()
        conn.close()

# Bucle para consultar datos cada 10 segundos
while True:
    query_data()
    sleep(10)
