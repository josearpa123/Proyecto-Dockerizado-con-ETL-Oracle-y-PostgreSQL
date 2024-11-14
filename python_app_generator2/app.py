import os
import psycopg2
import time
import random

# Configuración de conexión a PostgreSQL usando variables de entorno
db_host = os.getenv("DATABASE_HOST", "localhost")
db_name = os.getenv("DATABASE_NAME", "postgres")
db_user = os.getenv("DATABASE_USER", "user")
db_password = os.getenv("DATABASE_PASSWORD", "password")
db_port = os.getenv("DATABASE_PORT", "5432")

# Función para conectarse a la base de datos
def conectar():
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        print("Conexión a la base de datos establecida.")
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Intentar conexión inicial con reintentos
conn = None
while not conn:
    conn = conectar()
    if not conn:
        print("Reintentando en 2 segundos...")
        time.sleep(2)

# Inserción periódica de datos ficticios
while True:
    try:
        with conn.cursor() as cursor:
            nombre = f"Usuario_{random.randint(1000, 9999)}"
            correo = f"{nombre}@correo.com"
            cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)", (nombre, correo))
            conn.commit()
            print(f"Datos insertados: {nombre}, {correo}")
    except Exception as e:
        print(f"Error durante la inserción de datos: {e}")
        conn.rollback()

    time.sleep(10)  # Esperar 10 segundos antes de la siguiente inserción
s