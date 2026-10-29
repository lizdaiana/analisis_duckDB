
# Análisis de Datos Meteorológicos con DuckDB y SQL

## Descripción del proyecto

El objetivo de este proyecto es analizar datos meteorológicos mediante Python, SQL y DuckDB, consultando directamente un archivo CSV sin necesidad de utilizar una base de datos tradicional.

Para realizar dicho trabajo se utilizo un conjunto de datos meteorológicos provenientes de la pagina de NOAA correspondiente al año 2018, con registros diarios de la estación Denver International Airport, Colorado, Estados Unidos.

## Objetivos

- Consultar archivos CSV directamente con DuckDB.
- Aplicar limpieza básica de datos.
- Calcular estadísticas meteorológicas.
- Analizar temperaturas promedio y máximas.
- Identificar registros con temperaturas elevadas.
- Analizar datos de precipitación.

## Tecnologías utilizadas

-  Python
- DuckDB
- SQL
- pandas
- CSV

## Estructura del proyecto

    analisis_duckdb/
    ├── data/
    │   └── sample.csv
    ├── analisis_clima.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## Consultas analíticas

Se realizzaron las sigueites consultas:
1. Resumen general de registros y temperaturas disponibles.
2. Temperatura promedio mensual expresada en grados Celsius.
3. Temperatura máxima histórica por estación.
4. Filtrado de días con temperatura media superior a 30 °C.
5. Identificación de los diez registros con mayor precipitación.

## Limpieza de datos

Se tuvo que realizar la conversion de la columnas numéricas, ademas de expluir valores especiales que nos representan faltantes.

También, se realizo la transformacion de la temperadura de grados Fahrenheit a grado celsius, permitiendo una mejor interpretación.



## Instalación

Se requiere Python 3 y pip.

Instalar las dependencias con:

    pip install -r requirements.txt

## Ejecución

Desde la carpeta principal del proyecto, ejecutar:

    python analisis_clima.py

## Resultados

El programa muestra en la terminal los resultados de las cinco consultas SQL.

Los hallazgos y los tiempos de ejecución se documentarán después de ejecutar el análisis con el archivo CSV.
El resltado final que nos muestra la terminal, es lo siguiente
| Fecha | Estación meteorológica | Precipitación |
|---|---|---:|
| 2018-05-14 | DENVER INTERNATIONAL AIRPORT, CO US | 0.66 |
| 2018-05-03 | DENVER INTERNATIONAL AIRPORT, CO US | 0.64 |
| 2018-07-24 | DENVER INTERNATIONAL AIRPORT, CO US | 0.43 |
| 2018-08-15 | DENVER INTERNATIONAL AIRPORT, CO US | 0.38 |
| 2018-10-08 | DENVER INTERNATIONAL AIRPORT, CO US | 0.36 |
| 2018-03-19 | DENVER INTERNATIONAL AIRPORT, CO US | 0.33 |
| 2018-04-21 | DENVER INTERNATIONAL AIRPORT, CO US | 0.32 |
| 2018-03-27 | DENVER INTERNATIONAL AIRPORT, CO US | 0.32 |
| 2018-08-07 | DENVER INTERNATIONAL AIRPORT, CO US | 0.31 |
| 2018-03-29 | DENVER INTERNATIONAL AIRPORT, CO US | 0.31 |

## Uso de DuckDB

DuckDB consulta directamente el archivo CSV mediante SQL y crea una vista virtual.

Se utiliza una conexión en memoria, sin generar archivos binarios de bases de datos.

## Fuente de datos

NOAA - National Centers for Environmental Information.

https://www.ncei.noaa.gov/cdo-web/


