from django.shortcuts import render

from apps.news.models import SixforsixPublishedNews


# Views function for 6for6 index page of site
def sixforsix_index(request):
    sixforsix_latest_news_list = SixforsixPublishedNews.objects.order_by('-published_date')[:3]

    context = {'sixforsix_latest_news_list': sixforsix_latest_news_list,}

    return render(request, 'home/sixforsix_index.html', context)


