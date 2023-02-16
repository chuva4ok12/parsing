from pymongo import MongoClient
from lxml import html
import requests
client = MongoClient('127.0.0.1', 27017)
db = client['wonderful_herschel']
news_collection = db.news

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
url = 'https://yandex.ru/news/'
session = requests.Session()
response = session.get(url, headers=headers)
dom = html.fromstring(response.text)
source = dom.xpath("//div[contains(@class, 'news-top-flexible-stories')]//a[@class='mg-card__source-link']/text()")
name = dom.xpath("//div[contains(@class, 'news-top-flexible-stories')]//a[@class='mg-card__link']/text()")
link = dom.xpath("//div[contains(@class, 'news-top-flexible-stories')]//a[@class='mg-card__link']/@href")
date = dom.xpath("//div[contains(@class, 'news-top-flexible-stories')]//span[@class='mg-card-source__time']/text()")
for i in range(len(name)):
    news_collection.insert_one({
        'source': source[i],
        'name': name[i].replace('\xa0', ' '),
        'link': link[i],
        'date': date[i]
    })
for item in news_collection.find({}):
    print(item)
client.close()