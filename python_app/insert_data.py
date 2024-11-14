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

# Función para insertar datos
def insert_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    try:
        # Crear una tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                cargo VARCHAR(100)
            )
        """)
        conn.commit()

        # Insertar datos
        cursor.execute("""
            INSERT INTO empleados (nombre, cargo)
            VALUES (%s, %s)
        """, ('Juan Pérez', 'Desarrollador'))
        conn.commit()

        print("Datos insertados correctamente.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")
    finally:
        cursor.close()
        conn.close()

# Bucle para insertar empleados cada 10 segundos
while True:
    insert_data()
    sleep(10)
