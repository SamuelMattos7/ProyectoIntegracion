from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from django import forms


class RegistroUsuario(forms.ModelForm):
    
    # detalla campos a llenar 
    username = forms.CharField(label='cree su nombre de usuario', min_length=6, max_length=30, help_text='requerido')
    email = forms.EmailField(label='Ingrese su correo electronico', help_text='requerido', error_messages={'error':'debe ingresar un correo electronico'})
    password = forms.CharField(label='Ingrese su contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput)

    # Indica el modelo y los campos en el cual se ingresa la informacion
    class Meta:
        model = Usuario
        fields = ['username', 'email']

    # funciones que comprueban que los datos esten ingresados correctamente

    def check_username(self):
        username = self.cleaned_data['username'].lower() # toma el nombre de usurio ingresado en el formulario y lo tranforma todo a lowercase
        existe = Usuario.objects.filter(username=username) # valida que el nombre de usuario ingresado, no exista en la base de datos
        # si el username existe lanza error de validacion y indica el porque 
        if existe.count(): 
            raise forms.ValidationError('Este nombre de usuario ya existe')
        return username
    
    def check_email(self):
        email = self.cleaned_data['email'].lower()
        existe = Usuario.objects.filter(email=email)
        if existe.count(): 
            raise forms.ValidationError('Este nombre de email ya esta registrado')
        return email
    
    def check_password2(self):
        passw = self.cleaned_data
        if passw['password'] != passw['password2']:
            raise forms.ValidationError('Las contraseñas ingresadas no coinciden')
        return passw['password2']

class UsuarioLogin(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))