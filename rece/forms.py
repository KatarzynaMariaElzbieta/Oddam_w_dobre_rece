from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

        widgets = {
            'password': forms.PasswordInput,
        }

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Imię'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nazwisko'
        self.fields['password'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password2'].widget.attrs['placeholder'] = 'Powtórz hasło'


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))

