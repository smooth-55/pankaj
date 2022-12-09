from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(UserCreationForm):

    """
    adding extra fields in UserCreationForm
    """

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control entexam-input",
                "type": "password",
                "name": "password1",
                "placeholder": "Enter Password",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control entexam-input",
                "name": "password2",
                "placeholder": "Enter Confirm Password",
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            # "first_name",
            # "last_name",
            "password1",
            "password2",
        ]

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Enter Username",
                    "class": "form-control entexam-input",
                }
            ),
        }
