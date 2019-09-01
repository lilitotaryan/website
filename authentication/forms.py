from django import forms

class user_login(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)

class user_signup(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=200)
    last_name = forms.CharField(label='Last Name', max_length=200)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)