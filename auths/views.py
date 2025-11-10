from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, LoginForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro exitoso. Su cuenta será revisada por el administrador.')
            return redirect('auths:login')
    else:
        form = RegistroForm()
    return render(request, 'auths/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user.username}')
                return redirect('vehiculos:listar_vehiculos')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'auths/login.html', {'form': form})

from django.contrib.auth import logout
def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('auths:login')  # Redirige al login