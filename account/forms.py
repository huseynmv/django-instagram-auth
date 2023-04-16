from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=127, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'E-mail'}))
    password = forms.CharField(max_length=127, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'Password'}))