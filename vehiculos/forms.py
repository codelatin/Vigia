from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'nombre_vehiculo',
            'tipo_vehiculo',
            'placa',
            'imagen_vehiculo',
            'nombre_responsable',
            'rango_responsable',
            'observacion_mantenimiento'
        ]
        widgets = {
            'nombre_vehiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_vehiculo': forms.Select(attrs={'class': 'form-control'}),  # 👈 CAMBIA AQUÍ
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen_vehiculo': forms.FileInput(attrs={'class': 'form-control'}),
            'nombre_responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'rango_responsable': forms.Select(attrs={'class': 'form-control'}),  # ✅ OK
            'observacion_mantenimiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
