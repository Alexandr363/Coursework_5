from vacancy_util import get_employees


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
