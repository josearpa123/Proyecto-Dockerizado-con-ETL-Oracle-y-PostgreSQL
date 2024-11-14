# python_query_app/query_data.py

import psycopg2
import os

# Parámetros de conexión a la base de datos secundaria
DB_HOST = os.getenv("DATABASE_HOST", "postgres_replica")
DB_NAME = os.getenv("DATABASE_NAME", "postgres")
DB_USER = os.getenv("DATABASE_USER", "user")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")

def obtener_datos():
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        cursor = conn.cursor()

        # Consulta de ejemplo
        cursor.execute("SELECT * FROM usuarios;")
        registros = cursor.fetchall()

        cursor.close()
        conn.close()

        return registros
    except Exception as e:
        print(f"Error al conectar a la base de datos secundaria: {e}")
        return []
