from django import forms
from .models import Usuario,TipoUsuario


tp= TipoUsuario.objects.all()

class IniciarSesion(forms.Form):

    rut = forms.CharField(label='Rut')
    contraseña = forms.CharField(widget=forms.PasswordInput())


    rut.widget.attrs['class'] = 'form-control'
    contraseña.widget.attrs['class'] = 'form-control'

class userRegistrationForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    rut = forms.CharField(label='Rut')
    telefono = forms.CharField(label='Telefono')
    correo = forms.CharField(label='Correo electronico')
    contraseña = forms.CharField(widget=forms.PasswordInput())
    terminos = forms.BooleanField(label='', required=True, disabled=False, widget=forms.widgets.CheckboxInput(
        attrs={'class': 'checkbox-inline', 'value': False, 'name': 'terminos'}), help_text="Acepto los terminos y condiciones", error_messages={'required': 'Debe aceptar los terminos y condiciones para registrarse'})

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    contraseña.widget.attrs['class'] = 'form-control'
