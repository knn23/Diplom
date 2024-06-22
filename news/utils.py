import requests
from datetime import datetime
from .models import Article

NEWS_API_URL = 'https://newsapi.org/v2/everything'
API_KEY = '6a9652ccaa5641c5b3571e378ef5c3d3'  # Получите ключ API на https://newsapi.org/

def fetch_news():
    params = {
        'q': 'IT',
        'language': 'uk',
        'apiKey': API_KEY,
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    return data.get('articles', [])

def save_articles(articles):
    for article in articles:
        title = article.get('title')
        content = article.get('description', '')
        author = article.get('author', '')
        source = article.get('source', {}).get('name', '')
        published_at = article.get('publishedAt')
        url = article.get('url')

        if published_at:
            published_at = datetime.fromisoformat(published_at[:-1])  # Преобразование строки в datetime

        if title and content and published_at and url:
            Article.objects.update_or_create(
                title=title,
                defaults={
                    'content': content,
                    'author': author,
                    'source': source,
                    'published_at': published_at,
                    'url': url,
                }
            )
