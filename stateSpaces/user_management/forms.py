from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    display_name = forms.CharField(max_length=63)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = [
			'username',
            'display_name',
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',
        ]