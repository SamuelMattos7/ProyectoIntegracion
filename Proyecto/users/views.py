from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from .hash import Hash_Activacion_Cuenta
from users.form import RegistroUsuario
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

@login_required
def MenuUser(request):
    return render(request, 'usuario/MenuUser.html')

def Users(request):
    return render(request, 'users.html')

def Registro(request):

    if request.user.is_authenticated:
        return redirect('users')
    
    # Check de que el metodo de requerido sea POST y si lo es inicializa el formulario 
    if request.method == 'POST':

        form = RegistroUsuario(request.POST) 
        if form.is_valid():
            user = form.save(commit=False) # no se guarda al usuario de immediato 
            user.email = form.cleaned_data['email'] # se validida y limpia la informacion
            user.set_password(form.cleaned_data['password'])
            user.is_active = False # no se activa al usuario de immediato
            user.save()

            current_site = get_current_site(request)
            asunto = 'Activacion de Cuenta ReidioSolutions'
            mensaje = render_to_string('Activacion_Cuentas.html', 
                {
                    'user':user,
                    'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': Hash_Activacion_Cuenta.make_token(user),
                }
            )
            user.email_user(subject=asunto, message=mensaje)
        else:
            form = RegistroUsuario()
            return render(request, 'registro.html', {'form':form})
        
    form = RegistroUsuario()
    return render(request, 'registro.html', {'form': form})

def Activacion_Cuenta(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Usuario.objects.get(pk=uid)
    except():
        pass
    if user is not None and Hash_Activacion_Cuenta.check_token(user, token):
        user.is_active =True
        user.save()
        login(request, user)
        return redirect('users')
    else:
        return render(request, 'Activacion_Cuenta_Invalida.html')
