from django.shortcuts import render
from apps.news.models import News


# Views function for home page of site
def index(request):
    # news part
    latest_news = News.objects.order_by('-published_date')[:3]
    context = {'latest_news': latest_news,}
    return render(request, 'home/index.html', context)


# View function for admin page that nested in home page
def administraion(request):
    return render(request, 'home/include_admin.html')