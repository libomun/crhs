from django.shortcuts import render
from apps.news.models import SurgeConPublishedNews


# Views function for SurgeCon index page of site

def surgecon_index(request):
    surgecon_latest_news_list =SurgeConPublishedNews.objects.order_by('-published_date')[:3]

    context = {'surgecon_latest_news_list': surgecon_latest_news_list,}

    return render(request, 'home/surgecon_index.html', context)

