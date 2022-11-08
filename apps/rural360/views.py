from django.shortcuts import render

from apps.news.models import Rural360PublishedNews


# Views class for rural360 index page of site
def rural360index(request):
    rural360_latest_news_list = Rural360PublishedNews.objects.order_by('-published_date')[:3]

    context = {'rural360_latest_news_list': rural360_latest_news_list,}

    return render(request, 'home/rural360_index.html', context)