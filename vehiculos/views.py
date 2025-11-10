
# Create your views here.
# views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required


def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo registrado exitosamente.')
            return redirect('vehiculos:crear_vehiculo')  # Redirige a la misma página para registrar otro
    else:
        form = VehiculoForm()

    return render(request, 'vehiculos/crear_vehiculo.html', {'form': form})
@login_required
def listar_vehiculos(request):
    query = request.GET.get('q', '')
    vehiculos = Vehiculo.objects.all()

    if query:
        vehiculos = vehiculos.filter(placa__icontains=query)

    return render(request, 'vehiculos/listar_vehiculos.html', {
        'vehiculos': vehiculos,
        'query': query,
    })

def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo actualizado exitosamente.')
            return redirect('vehiculos:listar_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})
def eliminar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    vehiculo.delete()
    messages.success(request, 'Vehículo eliminado correctamente.')
    return redirect('vehiculos:listar_vehiculos')