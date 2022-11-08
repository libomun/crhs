from django.urls import path

from . import views

app_name = 'rural360'
urlpatterns = [
    path('', views.rural360index, name='rural360index'),
    ]