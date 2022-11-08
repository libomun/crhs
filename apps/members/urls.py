from django.urls import path

from . import views
app_name = 'members'
urlpatterns = [
    path('', views.MembersListView.as_view(), name='index'),
    path('faculty', views.FacultyListView.as_view(), name='faculty'),
    path('staff', views.StaffListView.as_view(), name='staff'),
    path('ra', views.RAListView.as_view(), name='ra'),
    path('graduate', views.GraduateListView.as_view(), name='graduate'),
    path('undergraduate', views.UndergradListView.as_view(), name='undergrad'),
    path('postdoc', views.PostdocListView.as_view(), name='postdoc'),
    path('<int:pk>/', views.MembersDetailView.as_view(), name='member_detail'),
    path('alumni', views.AlumniListView.as_view(), name='alumni'),
    path('alumni/<int:pk>/', views.AlumniDetailView.as_view(), name='alumni_detail'),
    path("search/", views.SearchMemberView.as_view(), name="search"),
]