import os
import psycopg2


def get_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def buscar_leituras_por_obra(obra_id):

    if obra_id is None:
        raise ValueError("obra_id nao pode ser nulo")

    if not isinstance(obra_id, int):
        raise TypeError("obra_id deve ser inteiro")

    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM leituras_sensores
                WHERE obra_id = %s
                """,
                (obra_id,),
            )

            return cursor.fetchall()
