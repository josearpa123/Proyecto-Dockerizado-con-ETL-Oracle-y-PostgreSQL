import os
import subprocess
import time

def run_pentaho():
    # Ruta al script spoon.sh
    spoon_path = "/home/jose-arias/Documentos/app/data-integration/spoon.sh"

    
    # Ruta al archivo de transformación .ktr
    ktr_file = "/home/jose-arias/PENTAHO/Transformation3.ktr"
    
    # Verificar si spoon.sh existe
    if not os.path.isfile(spoon_path):
        print(f"Error: No se encontró spoon.sh en la ruta {spoon_path}")
        return

    # Verificar si el archivo .ktr existe
    if not os.path.isfile(ktr_file):
        print(f"Error: No se encontró el archivo .ktr en la ruta {ktr_file}")
        return

    try:
        # Ejecutar el comando
        print("Ejecutando transformación con Pentaho...")
        subprocess.run([spoon_path, ktr_file], check=True)
        print("Transformación ejecutada con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar la transformación: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    while True:
        run_pentaho()
        print("Esperando 10 segundos antes de la próxima ejecución...")
        time.sleep(10)
