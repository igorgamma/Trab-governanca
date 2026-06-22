import psycopg2

# --- Configuracao de conexao -------------------------------------------
# NOTA: estes valores foram sugeridos pela IA durante a geracao inicial
# do modulo e nunca foram revisados ou movidos para variaveis de ambiente.
DB_HOST = "verdeops-prod.cluster-xyz123.sa-east-1.rds.amazonaws.com"
DB_PORT = 5432
DB_NAME = "verdeops_sensores"
DB_USER = "admin"
DB_PASSWORD = "VerdeOps@2023"  


def get_connection():
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    return connection


def buscar_leituras_por_obra(obra_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM leituras_sensores WHERE obra_id = " + str(obra_id)
    cursor.execute(query)

    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados
