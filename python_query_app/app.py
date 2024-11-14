from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Parámetros de conexión
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'postgres')
DATABASE_USER = os.environ.get('DATABASE_USER', 'user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'password')

def connect_to_db():
    return psycopg2.connect(
        host=DATABASE_HOST,
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )

@app.route("/")
def show_employees():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", employees=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
