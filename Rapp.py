import subprocess
import time

# Ruta del archivo .sh en formato Linux
sh_file_path = r"/home/config/Proyecto-Dockerizado-con-ETL-Oracle-y-PostgreSQL/DATA_INTEGRATION_REQ/PENTAHO/pentaho.sh"

while True:
    try:
        subprocess.run(['bash', sh_file_path], check=True)
        print("El archivo .sh se ejecutó correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error al ejecutar el archivo .sh: {e}")
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
    
    # Esperar 10 segundos antes de la siguiente ejecución
    time.sleep(10)
