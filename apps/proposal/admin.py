from django.contrib import admin
from .models import Team, References, Budget, WorkPlan, Appendices, Proposal


class TeamInline(admin.TabularInline):
    model = Team


class ReferencesInline(admin.TabularInline):
    model = References


class BudgetInline(admin.TabularInline):
    model = Budget


class WorkPlanInline(admin.TabularInline):
    model = WorkPlan


class AppendicesInline(admin.TabularInline):
    model = Appendices


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    inlines = [TeamInline, ReferencesInline, BudgetInline, WorkPlanInline, AppendicesInline]
