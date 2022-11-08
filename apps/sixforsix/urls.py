from django.urls import path

from . import views

app_name = 'sixforsix'
urlpatterns = [
    path('', views.sixforsix_index, name='sixforsix_index'),
    ]