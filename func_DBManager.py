from DBManager import DBManager


def func_dbmanager(db_name):
    """Реализует запрос к базе данных"""

    while True:
        print(
            f"Теперь можно сделать запрос к базе данных, выберете интересующий"
            f" вариант :\n"
            f"1. Получить список компаний и количество вакансий у каждой"
            f" компании\n"
            f"2. Получить список всех компаний с указанием названия компании,"
            f" названия \n   вакансии, зарплаты и ссылки на вакансию\n"
            f"3. Получить среднюю зарплату по вакансиям\n"
            f"4. Получить список всех вакансий, у которых зарплата выше средней"
            f" по всем \n   вакансиям\n"
            f"5. Получить список всех вакансий, в названии которых содержится "
            f"заданное\n   слово\n"
            f"0. Выход из программы")
        user = input('выберете действие: \n')
        if user == '0':
            break
        elif user == '1':
            DBManager.get_companies_and_vacancies_count(db_name)
        elif user == '2':
            DBManager.get_all_vacancies(db_name)
        elif user == '3':
            DBManager.get_avg_salary(db_name)
        elif user == '4':
            DBManager.get_vacancies_with_higher_salary(db_name)
        elif user == '5':
            text = input('Введите слово для поиска ')
            DBManager.get_vacancies_with_keyword(db_name, text)
