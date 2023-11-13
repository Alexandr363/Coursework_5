import psycopg2


class DBManager:

    @classmethod
    def get_companies_and_vacancies_count(cls, db_name):
        """Получает список всех компаний и количество вакансий у
        каждой компании"""
        conn = psycopg2.connect(dbname=db_name, host='localhost',
                                user='postgres', password='admin', port=5432)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("""SELECT company_name, vacancy_count 
                       FROM employees
                       ORDER BY company_name""")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()

    @classmethod
    def get_all_vacancies(cls, db_name):
        """Получает список всех вакансий с указанием названия компании, названия
        вакансии, зарплаты и ссылки на вакансию"""
        conn = psycopg2.connect(dbname=db_name, host='localhost',
                                user='postgres', password='admin', port=5432)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("""SELECT vacancy_name, company_name, vacancy_count,
                       salary, url_vacancy 
                       FROM vacancies
                       INNER JOIN employees USING(id_company)
                       ORDER BY company_name""")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()

    @classmethod
    def get_avg_salary(cls, db_name):
        """Получает среднюю зарплату по вакансиям."""

        conn = psycopg2.connect(dbname=db_name, host='localhost',
                                user='postgres', password='admin', port=5432)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("""SELECT AVG(salary) 
                       FROM vacancies
                       """)
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()

    @classmethod
    def get_vacancies_with_higher_salary(cls, db_name):
        """Получает список всех вакансий, у которых зарплата выше средней по
        всем вакансиям"""

        conn = psycopg2.connect(dbname=db_name, host='localhost',
                                user='postgres', password='admin', port=5432)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("""SELECT vacancy_name 
                       FROM vacancies
                       WHERE salary > ((SELECT AVG(salary)
                       FROM vacancies))                     
                       """)
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()

    @classmethod
    def get_vacancies_with_keyword(cls, db_name, text):
        """Получает список всех вакансий, в названии которых содержатся
        переданные в метод слова, например python"""

        conn = psycopg2.connect(dbname=db_name, host='localhost',
                                user='postgres', password='admin', port=5432)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT vacancy_name "
                    f"FROM vacancies "
                    f"WHERE vacancy_name LIKE '%{text}%'")

        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()
