from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path("news/search/", views.NewsSearchView.as_view(), name="news_search"),
    path('news/<int:pk>/comment/', views.AddCommentView.as_view(), name="add_comment"),
    ]