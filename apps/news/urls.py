from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path("news/search/", views.NewsSearchView.as_view(), name="news_search"),
    ]