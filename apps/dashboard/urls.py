from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard_base, name='dashboard_base'),
    path('profile', views.member_profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('article', views.article_list, name='article_list'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('presentation', views.presentation_list, name='presentation_list'),
    path('presentation/create/', views.presentation_create, name='presentation_create'),
    path('presentation/<int:pk>/edit/', views.presentation_edit, name='presentation_edit'),
    path('presentation/<int:pk>/delete/', views.presentation_delete, name='presentation_delete'),
    path('book', views.book_list, name='book_list'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('online', views.online_list, name='online_list'),
    path('online/create/', views.online_create, name='online_create'),
    path('online/<int:pk>/edit/', views.online_edit, name='online_edit'),
    path('online/<int:pk>/delete/', views.online_delete, name='online_delete'),
    ]