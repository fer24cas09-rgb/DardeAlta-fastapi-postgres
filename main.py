from fastapi import FastAPI, HTTPException
from config.database import get_connection

app = FastAPI(
    title="Clase SSR",
    description="Primera conexión entre FASTAPI y PostgreSQL",
    version="1.0"
)

@app.get("/db-test")
def probar_bd():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        current_database() AS base_datos,
                        current_user AS usuario,
                        now() AS fecha_hora;
                    """
                )
                resultado = cursor.fetchone()
                return {
                    "conexion": "correcto",
                    "informacion": resultado
                }
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"No fue posible conectarse con PostgreSQL: {error}"
        )

@app.get("/estudiantes")
def obtener_estudiantes():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        id,
                        nombre,
                        correo,
                        creado_en
                    FROM estudiantes
                    ORDER BY id;
                    """
                )
                estudiantes = cursor.fetchall()
                return estudiantes
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Conexión fallida: {error}"
        )

@app.get("/maestros")
def obtener_maestros():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        id,
                        nombre,
                        correo,
                        turno
                    FROM maestros
                    ORDER BY id;
                    """
                )
                maestros = cursor.fetchall()
                return maestros
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Conexión fallida: {error}"
        )

@app.get("/personal")
def obtener_personal():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        id,
                        nombre,
                        area,
                        turno
                    FROM personal
                    ORDER BY id;
                    """
                )
                personal = cursor.fetchall()
                return personal
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Conexión fallida: {error}"
        )