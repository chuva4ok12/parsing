# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем
# должность) с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько
# страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия. (можно прописать статично hh.ru или superjob.ru)
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна
# быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.
# Сохраните в json либо csv.


import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

# https://spb.hh.ru/search/vacancy?text=python&salary=&ored_clusters=true&enable_snippets=true

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '109.0.0.0 Safari/537.36'}
url = 'https://spb.hh.ru/search/vacancy'
vacancy_list = []
params = {'search_field': 'name', 'text': 'Python', 'page': 0}
while True:
    session = requests.Session()
    response = session.get(url=url, params=params, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    vacancy = dom.find_all('div', {'class': 'vacancy-serp-item__layout'})
    if len(vacancy) == 0:
        break
    params['page'] += 1
    for item in vacancy:
        vacancy_data = {}
        block_a = item.find('a', {'class': 'bloko-link'})
        href = block_a.get('href')
        name = block_a.text
        salary = item.find('span', {'class': 'bloko-header-section-3'})
        if salary:
            salary = salary.text
        vacancy_data['name'] = name
        vacancy_data['reference'] = href
        vacancy_data['where_published'] = 'hh.ru'
        salary_data = {}
        salary_value = (str(salary)).replace('\u202f', '')
        if salary_value[0].isdigit():
            re_minimum_maximum = re.compile(r'\d+')
            re_currency = re.compile(r'\w+')
            minimum = re_minimum_maximum.findall(salary_value)[0]
            maximum = re_minimum_maximum.findall(salary_value)[1]
            currency = re_currency.findall(salary_value)[-1]
            salary_data['minimum'] = int(minimum)
            salary_data['maximum'] = int(maximum)
            salary_data['currency'] = currency
            vacancy_data['salary'] = salary_data
        if salary_value[0] == 'о':
            re_minimum_maximum = re.compile(r'\d+')
            re_currency = re.compile(r'\w+')
            minimum = re_minimum_maximum.findall(salary_value)[0]
            currency = re_currency.findall(salary_value)[-1]
            salary_data['minimum'] = int(minimum)
            salary_data['currency'] = currency
            vacancy_data['salary'] = salary_data
        if salary_value[0] == 'д':
            re_minimum_maximum = re.compile(r'\d+')
            re_currency = re.compile(r'\w+')
            maximum = re_minimum_maximum.findall(salary_value)[0]
            currency = re_currency.findall(salary_value)[-1]
            salary_data['maximum'] = int(maximum)
            salary_data['currency'] = currency
            vacancy_data['salary'] = salary_data
        if salary_value == 'None':
            vacancy_data['salary'] = None
        vacancy_list.append(vacancy_data)
print(len(vacancy_list))
pprint(vacancy_list)
