from django.urls import path

from . import views

app_name = 'surgecon'
urlpatterns = [
    path('', views.surgecon_index, name='surgecon_index'),
    ]