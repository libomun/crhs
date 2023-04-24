from django.urls import path
from . import views

app_name = 'proposal'

urlpatterns = [
    path('', views.proposal_all, name='proposal_all'),
    path('proposals/draft/', views.draft_proposals, name='draft_proposals'),
    path('proposals/requiring_attention/', views.requiring_attention_proposals, name='requiring_attention_proposals'),
    path('proposals/under_review/', views.under_review_proposals, name='under_review_proposals'),
    path('proposals/post_review/', views.post_review_proposals, name='post_review_proposals'),
    path('proposals/withdrawn/', views.withdrawn_proposals, name='withdrawn_proposals'),

    path('create/', views.proposal_create, name='proposal_create'),
    path('<int:pk>/edit/', views.proposal_edit, name='proposal_edit'),
    path('<int:pk>/delete/', views.proposal_delete, name='proposal_delete'),
    path('teams/<int:proposal_id>/', views.team_list, name='team_list'),
    path('teams//create/<int:proposal_id>/', views.team_create, name='team_create'),
    path('teams/<int:pk>/<int:proposal_id>/edit/', views.team_edit, name='team_edit'),
    path('teams/<int:pk>/<int:proposal_id>/delete/', views.team_delete, name='team_delete'),

    path('references/<int:proposal_id>/', views.references_list, name='references_list'),
    path('references/create/<int:proposal_id>/', views.references_create, name='references_create'),
    path('references/<int:pk>/<int:proposal_id>/edit/', views.references_edit, name='references_edit'),
    path('references/<int:pk>/<int:proposal_id>/delete/', views.references_delete, name='references_delete'),

    path('budgets/<int:proposal_id>/', views.budget_list, name='budget_list'),
    path('budgets/create/<int:proposal_id>/', views.budget_create, name='budget_create'),
    path('budgets/<int:pk>/<int:proposal_id>/edit/', views.budget_edit, name='budget_edit'),
    path('budgets/<int:pk>/<int:proposal_id>/delete/', views.budget_delete, name='budget_delete'),

    path('workplans/<int:proposal_id>/', views.workplan_list, name='workplan_list'),
    path('workplans/create/<int:proposal_id>/', views.workplan_create, name='workplan_create'),
    path('workplans/<int:pk>/<int:proposal_id>/edit/', views.workplan_edit, name='workplan_edit'),
    path('workplans/<int:pk>/<int:proposal_id>/delete/', views.workplan_delete, name='workplan_delete'),

    path('appendices/<int:proposal_id>/', views.appendices_list, name='appendices_list'),
    path('appendices/create/<int:proposal_id>/', views.appendices_create, name='appendices_create'),
    path('appendices/<int:pk>/<int:proposal_id>/edit/', views.appendices_edit, name='appendices_edit'),
    path('appendices/<int:pk>/<int:proposal_id>/delete/', views.appendices_delete, name='appendices_delete'),

]
