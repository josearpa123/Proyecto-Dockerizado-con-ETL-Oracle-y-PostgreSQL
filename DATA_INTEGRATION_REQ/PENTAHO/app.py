import subprocess
import time

# Ruta del archivo .bat en formato Windows
bat_file_windows = r"\\wsl.localhost\Ubuntu-22.04\home\config\Proyecto-Dockerizado-con-ETL-Oracle-y-PostgreSQL\DATA_INTEGRATION_REQ\pentaho.bat"

while True:
    try:
        subprocess.run(['cmd.exe', '/c', bat_file_windows], check=True)
        print("El archivo .bat se ejecutó correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error al ejecutar el archivo .bat: {e}")
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
    
    # Esperar 10 segundos antes de la siguiente ejecución
    time.sleep(10)
