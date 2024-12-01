from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    birth_date = forms.DateField(widget=forms.SelectDateWidget)