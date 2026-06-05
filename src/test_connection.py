import psycopg2
from config import DB_CONFIG


def test_database_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("SELECT current_database();")
        database_name = cursor.fetchone()[0]

        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cursor.fetchall()

        print("Conexão realizada com sucesso!")
        print(f"Banco conectado: {database_name}")
        print("Tabelas encontradas:")

        for table in tables:
            print(f"- {table[0]}")

        cursor.close()
        conn.close()

    except Exception as error:
        print("Erro ao conectar no banco:")
        print(error)


if __name__ == "__main__":
    test_database_connection()