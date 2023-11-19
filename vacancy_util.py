import requests
from configparser import ConfigParser


def get_employees():
    """Получаем список работодателей"""

    url = 'https://api.hh.ru/employers/'
    response = requests.get(url, params={'area_id': 2,
                                         'specialization_id': 1.221,
                                         'per_page': 10,
                                         'only_with_vacancy': True,
                                         'sort_by': 'by_vacancies_open'})
    if response.status_code == 200:
        return response.json()


def vacancy(id_employee):
    """Получаем список вакансий по ID работодателя"""

    url = 'https://api.hh.ru/vacancies'
    response = requests.get(url, params={'area_id': 2,
                                         'only_with_salary': True,
                                         'per_page': 100,
                                         'employer_id': {id_employee}})
    if response.status_code == 200:
        return response.json()


def config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section,
                                                               filename))
    return db
