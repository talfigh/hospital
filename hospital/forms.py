from captcha.fields import CaptchaTextInput, CaptchaField
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'captcha/custom_field.html'


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
           attrs={
               "placeholder": "Username",
               "class": "form-control en",
               "autocomplete": "off",
               "tabindex": "1"
           }
        ),
        required=True
    )
    password = forms.CharField(
        min_length=6,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control en",
                "autocomplete": "off",
                "tabindex": "2"
            }
        ),
        required=True
    )

    captcha = CaptchaField(widget=CustomCaptchaTextInput)