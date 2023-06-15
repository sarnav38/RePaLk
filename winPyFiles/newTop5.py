import requests
import json

try:
    with open('config.json', 'r', encoding='utf-8') as f:
        api_key = json.load(f)['api_key']
except Exception:
    api_pro = 'enter api key in config.json file or config.json file not exsit'

def topNews(api_key: str = api_key, country: str = 'in') -> list:
    res = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}').json()
    top5News = []
    for i in range(5):
        top5News.append({'title': res['articles'][i]['title'],
                         'url': res['articles'][i]['url']})
    return top5News
