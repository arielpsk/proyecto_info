from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", required=True, widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username","email","password1","password2","first_name","last_name"]
        help_texts = { k:"" for k in fields }

class NoticiaCreateForm(forms.ModelForm):
    class Meta:
        model=Noticia
        fields=["titulo","subtitulo","texto","Categoria","imagen"]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Mot de passe incorrecte')
            if not user.is_active:
                raise forms.ValidationError('plus valide')
        return super(UserLoginForm, forms).clean(*args, **kwargs)

class ComentarioForm(forms.ModelForm):
    contenido = forms.CharField(required = True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comentario
        fields = (
            'contenido',
        )