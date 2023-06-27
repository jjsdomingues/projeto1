from django import forms

from django.contrib.auth.forms import UserCreationForm

class FormUser1(UserCreationForm):
    username = forms.CharField(label='Utilizador :', min_length=5, max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Entre 5 e 25 caracteres'}))
    email = forms.EmailField(label='E-mail :', widget=forms.TextInput(attrs={'placeholder': 'Introduza o seu e-mail'}))
    password1 =  forms.CharField(label='Password :', widget=forms.PasswordInput(attrs={'placeholder': 'Digite a sua password'}))
    password2 = forms.CharField(label='Confirmar :', widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a sua password'}))
    