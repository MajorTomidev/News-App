from django.shortcuts import render
from .models import News
# Create your views here.

def get_news(request):
    all_news = News.objects.all()

    context = {
        'all_news': all_news
    }

    return render(request, 'blog/tech-index.html', context)