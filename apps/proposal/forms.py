from django import forms
from .models import Proposal, Team, References, Budget, WorkPlan, Appendices
from django_select2 import forms as s2forms


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['title', 'abstract', 'background', 'project_history', 'data_collection', 'goal', 'audiences', 'impact', 'supervisor', 'pi', 'co_pi', 'referee', 'secretary', 'status']
        labels = {
            'project_history': 'Project History',
            'data_collection': 'Data Collection & Analysis',
            'goal': 'Goal & Strategy',
            'impact': 'Impact on Community',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'abstract': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'background': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'project_history': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'data_collection': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'goal': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'audiences': forms.Textarea(attrs={'class': 'form-control'}),
            'impact': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
             'supervisor': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
             'pi': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
             'co_pi': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
             'referee': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
             'secretary': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['first_name', 'last_name', 'degree', 'position', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        fields = ('doi', 'url', 'reference')
        widgets = {
            'doi': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'reference': forms.Textarea(attrs={'class': 'form-control'}),
        }


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('item', 'justification', 'cost')
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'justification': forms.Textarea(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class WorkPlanForm(forms.ModelForm):
    class Meta:
        model = WorkPlan
        fields = ('item', 'description', 'start_date', 'end_date', 'is_completed')
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AppendicesForm(forms.ModelForm):
    class Meta:
        model = Appendices
        fields = ('name', 'attachment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
        }
