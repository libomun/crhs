from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard_base, name='dashboard_base'),
    path('profile', views.member_profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('article', views.my_article, name='my_article'),
    path('presentation', views.my_presentation, name='my_presentation'),
    path('book', views.my_book, name='my_book'),
    path('online', views.my_online, name='my_online'),
    ]