import psycopg2
from vacancy_util import get_employees, vacancy


def create_database(db_name):
    """Создаём базу данных и 2 таблицы"""

    conn = psycopg2.connect(dbname='postgres', host='localhost',
                            user='postgres', password='admin', port=5432)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE {db_name}')
    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=db_name, host='localhost', user='postgres',
                            password='admin', port=5432)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("""CREATE TABLE employees (
                id_company INTEGER PRIMARY KEY,
                company_name VARCHAR,
                vacancy_count INTEGER,
                url_employees TEXT
                )
                """)

    cur.execute("""CREATE TABLE vacancies (
                id_vacancy INTEGER PRIMARY KEY,
                id_company INTEGER REFERENCES employees(id_company),
                vacancy_name VARCHAR,
                salary INTEGER,
                url_vacancy TEXT
                )
                """)
    cur.close()
    conn.close()


def db_load_data(db_name, user_employees):
    """Загружаем данные в таблицы"""

    employees = get_employees()
    conn = psycopg2.connect(dbname=db_name, host='localhost', user='postgres',
                            password='admin', port=5432)
    conn.autocommit = True
    cur = conn.cursor()

    for employee in employees['items']:
        cur.execute("""INSERT INTO  employees (
                    id_company, company_name, vacancy_count, url_employees)
                    VALUES (%s, %s, %s, %s)""",
                    (employee['id'],
                     employee['name'],
                     employee['open_vacancies'],
                     employee['alternate_url']))
    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=db_name, host='localhost', user='postgres',
                            password='admin', port=5432)
    conn.autocommit = True
    cur = conn.cursor()

    # user_employees - список выбранных юзером ID работодателей
    for id_employee in user_employees:
        emp_vac = vacancy(id_employee)['items']
        for emp in emp_vac:
            cur.execute("""INSERT INTO  vacancies (
                        id_vacancy, id_company, vacancy_name, salary,
                        url_vacancy)
                        VALUES (%s, %s, %s, %s, %s)""",
                        (emp['id'],
                         emp['employer']['id'],
                         emp['name'],
                         emp['salary']['from'],
                         emp['alternate_url']))
    cur.close()
    conn.close()
