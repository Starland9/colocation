from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
            "username",
            "password",
            "email",
            "birth_date",
            "sexe",
            "phone",
            "bio",
        ]
        widgets = {
            "password": forms.PasswordInput(),  # Add password widget
            "birth_date": forms.DateInput(
                attrs={"type": "date"}
            ),  # Add date input widget
        }
