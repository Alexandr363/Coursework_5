import requests


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
