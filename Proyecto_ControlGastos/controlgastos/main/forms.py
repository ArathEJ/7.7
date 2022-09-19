from django import forms
from .models import Usuario

class CreateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Usuario', 'Nombre', 'Correo']

class EditUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Usuario']