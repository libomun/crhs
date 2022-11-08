from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.AllNewsListView.as_view(), name='all_news_list'),
    path("search/", views.AllNewsSearchView.as_view(), name="all_news_search"),
    path('rural360/', views.Rural360NewsListView.as_view(), name='rural360_news_list'),
    path('rural360/<int:pk>/', views.Rural360NewsDetailView.as_view(), name='rural360_news_detail'),
    path("rural360/search/", views.Rural360NewsSearchView.as_view(), name="rural360_news_search"),
    path('sixforsix', views.SixforsixNewsListView.as_view(), name='sixforsix_news_list'),
    path('sixforsix/<int:pk>', views.SixforsixNewsDetailView.as_view(), name='sixforsix_news_detail'),
    path("sixforsix/search/", views.SixforsixNewsSearchView.as_view(), name="sixforsix_news_search"),
    path('surgecon', views.SurgeConNewsListView.as_view(), name='surgecon_news_list'),
    path('surgecon/<int:pk>', views.SurgeConNewsDetailView.as_view(), name='surgecon_news_detail'),
    path("surgecon/search/", views.SurgeConNewsSearchView.as_view(), name="surgecon_news_search"),
    ]