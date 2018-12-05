from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm, forms.ModelForm):
    """Class of form to register."""
    username = forms.CharField(label='Pseudo',max_length=25, required=True, widget=forms.TextInput(attrs={'class':'validate', 'data-length':'25', 'id':'pseudo'}), help_text='Lettres, chiffres et @ . + - _')
    first_name = forms.CharField(label='Prénom',max_length=30, required=False)
    last_name = forms.CharField(label='Nom',max_length=30, required=False)
    # email = forms.EmailField(max_length=254,required=True, help_text='Requis. Renseignez une adresse valide.')
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'validate', 'type':'email'}))
    password1 = forms.CharField(label='Mot de passe', required=True, widget=forms.PasswordInput(attrs={'id':'mdp1'}))
    password2 = forms.CharField(label='Mot de passe (confirmation)', required=True, widget=forms.PasswordInput(attrs={'id':'mdp2'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class SignUpFormCustom (forms.Form):
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'validate'}))
    username = forms.CharField(label='Pseudo', required=True, widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)
    # championnat = forms.ChoiceField(label='Championnat', required=True, widget=forms.Select())


class ChangeDataForm(forms.Form):
    email = forms.EmailField(label='Email', required=True, disabled=True, widget=forms.TextInput(attrs={'class':'validate'}))
    username = forms.CharField(label='Pseudo', required=True, disabled=True, widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)


class CodeForm (forms.Form):
    ia = forms.CharField(label='ia')


class ChampionshipForm(forms.Form):
    name = forms.CharField(label='Nom du championnat', max_length=60, required=True, widget=forms.TextInput(attrs={'class':'validate'}))
    secret_pass = forms.CharField(label='Code secret', max_length=60, required=False, widget=forms.TextInput(attrs={'type' : 'password'}), help_text='Créez un code secret.')
