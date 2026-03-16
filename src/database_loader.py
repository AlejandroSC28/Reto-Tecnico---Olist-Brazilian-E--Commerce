import sqlite3
import pandas as pd
import os

DB_DIR = r"C:\Users\SAMY10\Documents\Olist\datos\db"
DB_PATH = os.path.join(DB_DIR, "olist_warehouse.db")

def create_connection(db_file):
    """Crea una conexión a la base de datos SQLite."""
    conn = None
    try:
        os.makedirs(DB_DIR, exist_ok=True)
        conn = sqlite3.connect(db_file)
        print(f"----> Conexión establecida a SQLite: {db_file}")
    except Exception as e:
        print(f"----> Error conectando a la base de datos: {e}")
    return conn

def load_data_to_sqlite(conn):
    """Lee los CSVs y los inserta como tablas en SQLite."""
    
    tablas = {
        # Tablas de Dimensiones
        "dim_customers": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\customers_clean.csv",
        "dim_sellers": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\sellers_clean.csv",
        "dim_products": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\products_clean.csv",       
        "dim_geolocation": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\geolocation_clean.csv", 
        "dim_categories": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\categories_clean.csv", 
        
        # Tablas de Hechos
        "fact_orders": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\orders_clean.csv",          
        "fact_order_items": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\order_items_clean.csv",
        "fact_payments": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\payments_clean.csv",
        "fact_reviews": r"C:\Users\SAMY10\Documents\Olist\datos\limpios\reviews_clean.csv"
    }

    for table_name, csv_path in tablas.items():
        try:
            print(f"---> Cargando {table_name} desde {csv_path}...")
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"   ¡exito! {len(df)} filas insertadas.")
        except FileNotFoundError:
            print(f"   ---> ERROR: No se encontro el archivo {csv_path}. Verifica la ruta.")
        except Exception as e:
            print(f"   ---> ERROR inesperado al cargar {table_name}: {e}")

#Comprobamos la conección con un ejemplo

def test_database_connection(conn):
    """Ejecuta una consulta SQL de prueba con un doble JOIN."""
    print("\n Ejecutando prueba de validación SQL...")
    
    # Unimos las tablas (tambien se podrian unir directo en pandas), pero lo hacemos en SQL
    query = """
    SELECT 
        t.product_category_name_english AS categoria,
        COUNT(i.product_id) AS total_vendidos
    FROM fact_order_items i
    JOIN dim_products p ON i.product_id = p.product_id
    LEFT JOIN dim_categories t ON p.product_category_name = t.product_category_name
    GROUP BY categoria
    ORDER BY total_vendidos DESC
    LIMIT 3;
    """
    
    try:
        resultado = pd.read_sql_query(query, conn)
        print("==== Top 3 Categorías más vendidas (Validación exitosa):  ====")
        print(resultado)
    except Exception as e:
        print(f"=== Error en la consulta de validación: {e} ===")

if __name__ == "__main__":
    print("=== INICIANDO PIPELINE DE CARGA A BASE DE DATOS ===")
    conexion = create_connection(DB_PATH)
    
    if conexion:
        load_data_to_sqlite(conexion)
        test_database_connection(conexion)
        conexion.close()
        print("\n----> Proceso finalizado. Conexión cerrada.")