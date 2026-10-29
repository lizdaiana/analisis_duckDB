from pathlib import Path
import duckdb

# Ruta de la carpeta del proyecto
INICIO = Path(__file__).resolve().parent
CSV_PATH = INICIO / "data" / "sample.csv"

if not CSV_PATH.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo: {CSV_PATH}"
    )

# Conexión en memoria: no crea una base de datos en disco
con = duckdb.connect(database=":memory:")

try:
    # Leer el CSV directamente y crear una vista virtual
    ruta_csv = str(CSV_PATH).replace("\\", "/").replace("'", "''")

    con.execute(f"""
        CREATE VIEW clima AS
        SELECT
            TRY_CAST("DATE" AS DATE) AS fecha,
            "NAME" AS estacion,

            CASE
                WHEN TRY_CAST("TEMP" AS DOUBLE)
                     BETWEEN -100 AND 150
                THEN TRY_CAST("TEMP" AS DOUBLE)
                ELSE NULL
            END AS temperatura_f,

            CASE
                WHEN TRY_CAST("MAX" AS DOUBLE)
                     BETWEEN -100 AND 150
                THEN TRY_CAST("MAX" AS DOUBLE)
                ELSE NULL
            END AS maxima_f,

            CASE
                WHEN TRY_CAST("MIN" AS DOUBLE)
                     BETWEEN -100 AND 150
                THEN TRY_CAST("MIN" AS DOUBLE)
                ELSE NULL
            END AS minima_f,

            CASE
                WHEN TRY_CAST("PRCP" AS DOUBLE)
                     BETWEEN 0 AND 100
                THEN TRY_CAST("PRCP" AS DOUBLE)
                ELSE NULL
            END AS precipitacion

        FROM read_csv_auto('{ruta_csv}', header = true)
    """)

    # CONSULTA 1: resumen general
    print("\\n1. RESUMEN GENERAL")

    resultado = con.execute("""
        SELECT
            COUNT(*) AS total_registros,
            COUNT(temperatura_f) AS temperaturas_validas,
            COUNT(*) - COUNT(temperatura_f) AS temperaturas_nulas,
            COUNT(DISTINCT estacion) AS estaciones
        FROM clima
    """).df()

    print(resultado.to_string(index=False))

    # CONSULTA 2: temperatura promedio mensual
    print("\\n2. TEMPERATURA PROMEDIO POR MES (°C)")

    resultado = con.execute("""
        SELECT
            DATE_TRUNC('month', fecha)::DATE AS mes,
            ROUND(AVG((temperatura_f - 32) * 5.0 / 9.0), 2)
                AS promedio_celsius
        FROM clima
        WHERE fecha IS NOT NULL
          AND temperatura_f IS NOT NULL
        GROUP BY mes
        ORDER BY mes
    """).df()

    print(resultado.to_string(index=False))

    # CONSULTA 3: máximas históricas por estación
    print("\\n3. TEMPERATURA MÁXIMA POR ESTACIÓN (°C)")

    resultado = con.execute("""
        SELECT
            estacion,
            ROUND(
                (MAX(maxima_f) - 32) * 5.0 / 9.0,
                2
            ) AS maxima_celsius
        FROM clima
        WHERE maxima_f IS NOT NULL
        GROUP BY estacion
        ORDER BY maxima_celsius DESC
    """).df()

    print(resultado.to_string(index=False))

    # CONSULTA 4: días con temperatura media superior a 30 °C
    print("\\n4. DÍAS CON TEMPERATURA MEDIA SUPERIOR A 30 °C")

    resultado = con.execute("""
        SELECT
            fecha,
            estacion,
            ROUND(
                (temperatura_f - 32) * 5.0 / 9.0,
                2
            ) AS temperatura_celsius
        FROM clima
        WHERE temperatura_f > 86
          AND fecha IS NOT NULL
        ORDER BY temperatura_f DESC
    """).df()

    if resultado.empty:
        print("No se encontraron registros.")
    else:
        print(resultado.to_string(index=False))

    # CONSULTA 5: días con mayor precipitación
    print("\\n5. DÍAS CON MAYOR PRECIPITACIÓN")

    resultado = con.execute("""
        SELECT
            fecha,
            estacion,
            precipitacion
        FROM clima
        WHERE precipitacion IS NOT NULL
        ORDER BY precipitacion DESC
        LIMIT 10
    """).df()

    print(resultado.to_string(index=False))

    print("\\nAnálisis finalizado correctamente.")

finally:
    con.close()
    
