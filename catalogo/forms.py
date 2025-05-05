from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Libro

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'estado', 'resena']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
}