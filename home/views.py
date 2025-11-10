from django.shortcuts import render

# Create your views here.
# home/views.py

def home(request):
    # puedes pasar contexto si quieres
    context = {'titulo': 'Inicio - Plataforma MANTENET'} 
    return render(request, 'home/home.html', context)
