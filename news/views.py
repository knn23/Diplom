from django.shortcuts import render
from .models import Article
from .utils import fetch_news, save_articles

def news_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'news/news_list.html', context)

# views.py

from django.shortcuts import render, redirect
from .models import Article

def update_news(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = Article(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('news-list')
    else:
        form = Article(instance=article)
    return render(request, 'update_news.html', {'form': form})

