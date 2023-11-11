import psycopg2


def create_database(db_name):
    conn = None
    conn = psycopg2.connect(dbname='postgres', host='localhost',
                            user='postgres', password='admin', port=5432)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE {db_name}')
    conn.close()

    conn = psycopg2.connect(dbname=db_name, host='localhost', user='postgres',
                            password='admin', port=5432)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("""CREATE TABLE vacancies (
                id_vacancy INTEGER,
                id_company INTEGER PRIMARY KEY,
                vacancy_name VARCHAR,
                salary INTEGER,
                url_vacancy TEXT
                )
                """)

    cur.execute("""CREATE TABLE employees (
                id_company INTEGER PRIMARY KEY,
                company_name VARCHAR,
                vacancy_count INTEGER,
                url_employees TEXT
                )
                """)
    cur.close()
    conn.close()
