from django import forms

class login(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput)

class signup(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=200)
    last_name = forms.CharField(label='last_name', max_length=200)
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput)