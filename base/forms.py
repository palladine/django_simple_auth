from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label='Имя пользователя', widget=forms.widgets.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.widgets.PasswordInput())
