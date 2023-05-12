from django import forms
from .models import Members


class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['first_name', 'last_name', 'title', 'affiliation', 'profile_pic', 'email', 'phone', 'office_address', 'bio', 'external_link', 'role', 'is_active']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
