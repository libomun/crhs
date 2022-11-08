from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from apps.news.models import Rural360PublishedNews, SixforsixPublishedNews, SurgeConPublishedNews


# Views function for home page of site
def index(request):
    # news part
    rural360_latest_news = Rural360PublishedNews.objects.latest('published_date')
    sixfor6_latest_news = SixforsixPublishedNews.objects.latest('published_date')
    surgecon_latest_news = SurgeConPublishedNews.objects.latest('published_date')

    context = {'rural360_latest_news': rural360_latest_news,
               'sixfor6_latest_news': sixfor6_latest_news,
               'surgecon_latest_news': surgecon_latest_news,}

    return render(request, 'home/index.html', context)


# View function for admin page that nested in home page
def administraion(request):
    return render(request, 'home/include_admin.html')