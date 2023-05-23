from django.db.models import Q
from django.shortcuts import render
from apps.news.models import News, HeadlineNews, BottomInfo


# Views function for home page of site
def index(request):
    # news part
    latest_news = News.objects.order_by('-published_date')[:3]
    headlines = HeadlineNews.objects.filter(is_publish=True)
    headline1 = headlines.get(headline="headline1")
    headline2 = headlines.get(headline="headline2")
    headline3 = headlines.get(headline="headline3")
    bottominfos = BottomInfo.objects.filter(is_publish=True)
    info1 = bottominfos.get(bottom_info="info1")
    info2 = bottominfos.get(bottom_info="info2")
    info3 = bottominfos.get(bottom_info="info3")

    context = {'latest_news': latest_news,
               'headline1': headline1,
               'headline2': headline2,
               'headline3': headline3,
               'info1': info1,
               'info2': info2,
               'info3': info3,
               }
    return render(request, 'home/index.html', context)


# View function for admin page that nested in home page
def administraion(request):
    return render(request, 'home/include_admin.html')