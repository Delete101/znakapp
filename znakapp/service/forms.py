from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='')
    email = forms.EmailField(required=True, help_text='Пример: test@gmail.com')
    password1 = forms.CharField(label='Пароль', help_text='Не должен начинаться с цифр')
    password2 = forms.CharField(label='Повторите пароль', help_text=' ')

    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    error_css_class = 'class-error'
    required_css_class = 'class-required'
