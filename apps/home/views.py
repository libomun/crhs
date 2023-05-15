from django.shortcuts import render
from apps.news.models import News


# Views function for home page of site
def index(request):
    # news part
    latest_news = News.objects.order_by('-published_date')[:3]
    headlines = News.objects.filter(is_headline=True).order_by('-published_date')[:3]
    headline1 = headlines[0]
    headline2 = headlines[1]
    headline3 = headlines[2]

    context = {'latest_news': latest_news,
               'headline1': headline1,
               'headline2': headline2,
               'headline3': headline3}
    return render(request, 'home/index.html', context)


# View function for admin page that nested in home page
def administraion(request):
    return render(request, 'home/include_admin.html')