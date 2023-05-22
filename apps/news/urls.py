from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path("news/search/", views.NewsSearchView.as_view(), name="news_search"),
    path('news/<int:pk>/comment/', views.create_comment, name="add_comment"),
    path('news/<int:pk>/comment/<int:parent_comment_id>/', views.create_comment, name='create_reply'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    ]