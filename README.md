# Olist E-commerce Data Pipeline & Analytics

## 1. Descripción del Proyecto

El proyecto implementa un pipeline de datos end-to-end utilizando el dataset público de Olist (e-commerce brasileño). Abarca desde la extracción y limpieza de datos crudos, pasando por el modelado dimensional en una base de datos relacional, hasta la visualización y respuesta a preguntas clave de negocio.

## 2. Arquitectura y Fases del Proyecto
   
**Fase 1: Análisis Exploratorio de Datos (EDA)**
- Diagnóstico inicial de calidad de datos.
- Análisis de distribuciones y detección de valores atípicos (outliers) orientados al negocio.

**Fase 2: Limpieza y Transformación**
- Conversión de tipos de datos temporales.
- Correcciones ortográficas de columnas.
- Resolución de problemas de duplicados (en la tabla de geolocalización).
- Imputación estratégica de valores nulos para evitar la pérdida de métricas financieras.
- Valores atípicos(identificación)
        
**Fase 3: Modelado y Carga de Datos (Data Warehouse)**
- Diseño de un esquema en estrella (Star Schema) compuesto por tablas de hechos y dimensiones.
- Implementación de un script automatizado en Python para construir e insertar los datos limpios en una base de datos SQLite local.

**Fase 4: Análisis de Negocio (Dashboard)**
- Consultas SQL directas al modelo dimensional.
- Visualización de métricas con Python (Seaborn/Matplotlib) para responder a 5 preguntas estratégicas, incluyendo estacionalidad, top de categorías por ingresos, tiempos de entrega, tasa de incidencias y análisis logístico por estado.

**Fase 5: Orquestación**
- Script principal diseñado para ejecutar el pipeline de carga con un solo comando, asegurando la reproducibilidad del entorno.

## 3. Estructura del Repositorio

```text
proyecto_olist/  
 -- datos/
    -- db/       # Base de datos SQLite autogenerada (.db)
    -- limpios/  # Datasets procesados tras la Fase 2 (.csv)
    -- originales/   # Datasets originales de Kaggle (.csv)
 -- notebooks/
    -- exploración_y_diagnostico.ipynb   # Fase 1: EDA
    -- limpieza_y_transformación.ipynb      # Fase 2: Transformación de datos
    -- visualización_y_dashboard.ipynb  # Fase 4: Consultas SQL y visualizaciones
 -- src/
    -- database_loader.py # Fase 3: Script de conexión y carga ETL
 -- main.py               # Fase 5: Orquestador del pipeline
 -- README.md             # Documentación del proyecto
```

## 4. Instrucciones de Reproducción

Para evaluar este proyecto localmente, asegúrese de tener instalado Python 3.8 o superior y las librerías requeridas (pandas, matplotlib, seaborn).


**Paso 1: Clonar el repositorio**
```bash
git clone [https://github.com/AlejandroSC28/Reto-Tecnico---Olist-Brazilian-E--Commerce.git](https://github.com/AlejandroSC28/Reto-Tecnico---Olist-Brazilian-E--Commerce.git)
cd Reto-Tecnico---Olist-Brazilian-E--Commerce
```

**Paso 2: Ejecutar el pipeline de datos**
Este comando construirá la base de datos SQLite y cargará los archivos procesados automáticamente.
```bash
python main.py
```
   
**Paso 3: Visualizar los resultados de negocio**
Abra el archivo `notebooks/visualización_y_dashboard.ipynb` y ejecute todas las celdas para visualizar las consultas SQL y los gráficos que responden a las preguntas.

## 5. Tecnologías Utilizadas
- Lenguajes: Python, SQL
- Procesamiento de Datos: Pandas, Numpy
- Base de Datos: SQLite (Elegida para garantizar la reproducibilidad sin configuración de servidores externos)
- Visualización: Matplotlib, Seaborn, Missingno

    
