from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from .models import Rural360PublishedNews, SixforsixPublishedNews, SurgeConPublishedNews


# View class for all news list page
class AllNewsListView(generic.ListView):
    template_name = 'news/all_news_list.html'
    paginate_by = 3 # show Rural360 number in one page

    def get_queryset(self):
        return Rural360PublishedNews.objects.filter(is_publish=True).union(SixforsixPublishedNews.objects.filter(is_publish=True),SurgeConPublishedNews.objects.filter(is_publish=True)).order_by('-published_date')


# Search all news view
class AllNewsSearchView(generic.ListView):
    paginate_by = 3
    template_name = 'news/all_news_search_result.html'

# Return search all news result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Rural360PublishedNews.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(news_text__icontains=query) | Q(published_date__icontains=query)
            ).union(SixforsixPublishedNews.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(news_text__icontains=query) | Q(published_date__icontains=query)
            ), SurgeConPublishedNews.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(news_text__icontains=query) | Q(published_date__icontains=query)
            )).order_by('-published_date')
        return object_list

# Add query content in the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


# Rural360 news list view
class Rural360NewsListView(generic.ListView):
    template_name = 'news/rural360_news_list.html'
    queryset =Rural360PublishedNews.objects.filter(is_publish=True).order_by('-published_date')  # ordering by latest published time
    paginate_by = 3  # show Rural360 number in one page


# Rural360 news detail View
class Rural360NewsDetailView(generic.DetailView):
    model =Rural360PublishedNews
    template_name = 'news/news_detail.html'


# Rural360 news search view
class Rural360NewsSearchView(generic.ListView):
    paginate_by = 3
    template_name = 'news/rural360_news_search_result.html'

# Return search result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Rural360PublishedNews.objects.order_by('-published_date').filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(news_text__icontains=query) | Q(published_date__icontains=query)
            )
        return object_list

# Add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


# 6for6 news list view
class SixforsixNewsListView(generic.ListView):
    template_name = 'news/sixforsix_news_list.html'
    queryset =SixforsixPublishedNews.objects.filter(is_publish=True).order_by('-published_date')  # ordering by latest published time
    paginate_by = 3


# 6for6 news detail View
class SixforsixNewsDetailView(generic.DetailView):
    model =SixforsixPublishedNews
    template_name = 'news/news_detail.html'


# 6for6 search news view
class SixforsixNewsSearchView(generic.ListView):
    paginate_by = 3
    template_name = 'news/sixforsix_news_search_result.html'

# Return search result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = SixforsixPublishedNews.objects.order_by('-published_date').filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(news_text__icontains=query) | Q(published_date__icontains=query)
            )
        return object_list

# Add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


# SurgeCon news list view
class SurgeConNewsListView(generic.ListView):
    template_name = 'news/surgecon_news_list.html'
    queryset =SurgeConPublishedNews.objects.filter(is_publish=True).order_by('-published_date')  # ordering by latest published time
    paginate_by = 3


# SurgeCon news detail View
class SurgeConNewsDetailView(generic.DetailView):
    model =SurgeConPublishedNews
    template_name = 'news/news_detail.html'


# SurgeCon search news view
class SurgeConNewsSearchView(generic.ListView):
    paginate_by = 3
    template_name = 'news/surgecon_news_search_result.html'

# Return search result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = SurgeConPublishedNews.objects.order_by('-published_date').filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(news_text__icontains=query) | Q(published_date__icontains=query)
            )
        return object_list

# Add query content in  context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context