from django import forms
from django.contrib.auth.forms import UserCreationForm

class User(UserCreationForm):
    email=forms.EmailField(
        label="entrer votre email",
        required=True,
        widget=forms.TextInput(attrs={'autocomplte': 'email'}),
    
        
    )
    password1=forms.CharField(
        label="entrer votre password",
        required=True,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'})
    )
    password2=forms.CharField(
        label="confirmation votre password",
        required=True,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'})
    )

    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields +("password1","password2")

    