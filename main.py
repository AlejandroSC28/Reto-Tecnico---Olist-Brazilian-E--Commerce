import subprocess
import sys
import os


def ejecutar_script(ruta_script, descripcion):
    """Esya es una función auxiliar para ejecutar scripts de Python y manejar errores."""
    print(f"\n ---> PASO: {descripcion}...")
    try:
        # asegura que usemos el mismo entorno de Python actual
        subprocess.run([sys.executable, ruta_script], check=True)
        print(f"---> EXITO: {descripcion} completado.")
    except subprocess.CalledProcessError:
        print(f"---> ERROR: Fallo la ejecución de {ruta_script}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"---> ERROR: No se encontro el archivo {ruta_script}. ¿Estás ejecutando main.py desde la raíz del proyecto?")
        sys.exit(1)

def run_pipeline():
    print("="*60)
    print(" INICIANDO ORQUESTADOR DE PIPELINE - PROYECTO OLIST ")
    print("="*60)

    # Nota: Si convertimos el proceso de limpieza a un script.py, lo agregariamos aqui primero.
    # Por ahora, ejecutamos directamente 'Carga de BD' asumiendo que los CSVs limpios ya existen.
    
    # Ruta a el script
    script_bd = os.path.join("src", "database_loader.py")
    
    ejecutar_script(script_bd, "Creando Data Warehouse y Cargando Datos (SQLite)")

    print("\n" + "="*60)
    print("!PIPELINE FINALIZADO CORRECTAMENTE! ")
    print("El Data Warehouse (olist_warehouse.db) está actualizado y listo para análisis.")
    print("Siguiente paso: Abre el notebook 'Visualización_y_dashboard.ipynb' que se encuentra en la carpeta de 'notebooks' para explorar el reporte de negocio.")
    print("="*60)

if __name__ == "__main__":
    run_pipeline()