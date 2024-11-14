FROM python:3.9.20-alpine3.19

WORKDIR /app

# Instalar dependencias del sistema para psycopg2
RUN apk add --no-cache gcc libc-dev postgresql-dev

# Copiar archivos de la aplicación
COPY requirements.txt /app
COPY app.py /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
