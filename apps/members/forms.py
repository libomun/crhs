from django import forms
from .models import Members
from allauth.account.forms import SignupForm


class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['first_name', 'last_name', 'title', 'affiliation', 'profile_pic', 'email', 'phone', 'office_address', 'bio', 'external_link', 'role', 'is_active']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'affiliation': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'office_address': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'external_link': forms.URLInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }


# customer signupForm
class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        if user is not None:
            member = Members.objects.create(user=user,
                                            first_name=self.cleaned_data.get('first_name'),
                                            last_name=self.cleaned_data.get('last_name'))
            member.save()

        return user
