from django.urls import path

from . import views

app_name = 'publication'

urlpatterns = [
    path('articles/', views.ArticlesListView.as_view(), name='article_list'),
    path("<int:pk>/", views.ArticlesDetailView.as_view(), name="article_detail"),
    path("search/", views.ArticlesSearchView.as_view(), name="article_search"),

    path('presentation/', views.PresentationListView.as_view(), name='pre_list'),
    path("presentation/<int:pk>/", views.PresentationDetailView.as_view(), name="pre_detail"),
    path("presentation/search/", views.PresentationSearchView.as_view(), name="pre_search"),

    path('book/', views.BookListView.as_view(), name='book_list'),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("book/search/", views.BookSearchView.as_view(), name="book_search"),

    path('online/', views.OnlineListView.as_view(), name='online_list'),
    path("online/<int:pk>/", views.OnlineDetailView.as_view(), name="online_detail"),
    path("online/search/", views.OnlineSearchView.as_view(), name="online_search"),
    ]