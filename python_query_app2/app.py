# python_query_app/app.py

from flask import Flask, render_template, jsonify
from query_data import obtener_datos

app = Flask(__name__)

@app.route('/')
def index():
    datos = obtener_datos()
    return render_template('index.html', datos=datos)

@app.route('/api/datos')
def api_datos():
    datos = obtener_datos()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
