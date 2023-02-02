# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '109.0.0.0 Safari/537.36'}
params = {'login': 'chuva4ok12'}
url = 'https://api.github.com/users/chuva4ok12/repos'

response = requests.get(url, headers=headers, params=params)
j_data = response.json()

repos = []
for item in j_data:
    repos.append(item['name'])
print(f"The user {params['login']} has the following repos: {repos}")

filename = 'repos.json'
with open(filename, 'w') as f:
    json.dump(repos, f)

