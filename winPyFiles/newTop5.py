import requests, os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
api_key = os.environ['NEWS_API_KEY']

def topNews(api_key: str = api_key, country: str = 'in') -> list:
    res = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}').json()
    top5News = []
    for i in range(5):
        top5News.append({'title': res['articles'][i]['title'],
                         'url': res['articles'][i]['url']})
    return top5News
