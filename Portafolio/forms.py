from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proyecto

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña',widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

class ProyectoForm(forms.ModelForm):
    foto = forms.URLField()
    titulo_proyecto = forms.Textarea()
    desc_proyecto = forms.Textarea()
    tags = forms.Textarea()
    url_github = forms.URLField()

    class Meta:
        model = Proyecto
        fields = ['foto','titulo_proyecto','desc_proyecto','tags','url_github']