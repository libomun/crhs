from django import forms
from .models import Articles, Presentations, Books, Online
from django_select2 import forms as s2forms


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ['creator']  # Exclude the 'creator' field from the form

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'co_editor': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'author_list': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'doi': forms.TextInput(attrs={'class': 'form-control'}),
            'affiliation': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'journal': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'keywords': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PresentationsForm(forms.ModelForm):
    class Meta:
        model = Presentations
        exclude = ['creator']  # Exclude the 'creator' field from the form

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'co_editor': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'author_list': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'types': forms.Select(attrs={'class': 'form-control'}),
            'external_link': forms.URLInput(attrs={'class': 'form-control'}),
            'archive': forms.FileInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ['creator']  # Exclude the 'creator' field from the form

        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'co_editor': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'author_list': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'external_link': forms.URLInput(attrs={'class': 'form-control'}),
            'archive': forms.FileInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'categories': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OnlineForm(forms.ModelForm):
    class Meta:
        model = Online
        exclude = ['creator']  # Exclude the 'creator' field from the form

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'co_editor': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'author_list': s2forms.Select2MultipleWidget(attrs={'data-maximum-selection-length': 100}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'external_link': forms.URLInput(attrs={'class': 'form-control'}),
        }
