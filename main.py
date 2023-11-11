from vacancy_util import get_employees
from database_utils import create_database, db_load_data

vacancy = []
func_employee = get_employees()

# Выводим список работодателей
for i in range(len(func_employee)):
    # записываем все ID работодателей для дальнейшей сверки с выбором юзера
    vacancy.append(func_employee['items'][i]['id'])
    print(f"Компания {func_employee['items'][i]['name']}  "
          f"id = {func_employee['items'][i]['id']}  "
          f"вакансий {func_employee['items'][i]['open_vacancies']}\n"
          f"ссылка на компанию  {func_employee['items'][i]['alternate_url']}")
    print()

user_employees = []

# Юзер выбирает ID работодателей для получения вакансий
while True:
    user = input('выберете id компании или введите 0 для выхода: \n')
    if user == '0':
        break
    if user in vacancy:
        user_employees.append(user)
    else:
        print('неверно введён id')
    print(f'количество выбранных компаний:  {len(user_employees)}')
print()

# Создаём базу данных
db_name = input('Введите название базы данных: ')
create_database(db_name)
print(f"Создана база данных {db_name} и две таблицы: employees и  vacancies")

# Загружаем данные в таблицы
db_load_data(db_name, user_employees=user_employees)
print('Данные загружены в таблицы')
