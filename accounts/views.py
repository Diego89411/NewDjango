import email
from multiprocessing import context
from ssl import _PasswordType
from django.shortcuts import render

# Create your views here.

def registrarse(request):
    context
    if request.method == 'POST':
        password = request.POST['password']
        confirmPassword = request.POST['password']
        username = request.POST['username']
        emailUsuario = request.POST['emailUsuario']
        
        #validacion de campos
        if not emailUsuario:
            context['alarma'] = 'Ingrese el correo electronico'
        if not password or len(password) < 5:
            context['alarma'] = 'Ingrese un password de cinco(5) o mas caracteres'
        if not confirmPassword:
            context['alarma'] = '¡El password no coincide!'

        #todo ok
        existe = Account.objects.filter(email=email).exists()
        if not existe:
            user = Account.objects.create_user(first_name=username, last_name=username, email=email, password=password)
            user.save()
            context['mensaje'] = 'Usuario guardado con exito!'
        else:
            context['alarma'] = '¡El correo ya existe!'



    return render(request, 'registro.html', context)

    #************************CONTROL DE INGRESO DE USUARIOS*********************
    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authentication(email= email, password = password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'home.html')
            else:
                return render(request, 'usuarios/login.html') 
        else:
            return render((request), 'usuarios/login.html')        
