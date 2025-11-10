
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    # Opciones de rango militar
    RANGO_CHOICES = [
        ('soldado', 'Soldado Profesional'),
        ('cabo', 'Cabo'),
        ('suboficial', 'Suboficial'),
        ('sargento', 'Sargento'),
        ('tecnico', 'Técnico de Mantenimiento'),
        ('supervisor', 'Supervisor'),
        ('jefe', 'Jefe de Unidad'),
        ('comandante', 'Comandante'),
    ]
    VEHICULO_CHOICES =[
    ('camioneta', 'Camioneta'),
    ('tanque', 'Tanque'),   
    ('moto', 'Moto'),
    ('helicoptero', 'Helicóptero'),
    ('avion', 'Avión'),
    ('ambulancia', 'Ambulancia'),
]
    nombre_vehiculo = models.CharField(max_length=100, verbose_name="Nombre del Vehículo")
    tipo_vehiculo = models.CharField(max_length=50, choices=VEHICULO_CHOICES,verbose_name="Tipo de Vehículo",)
    placa = models.CharField(max_length=20, unique=True, verbose_name="Placa del Vehículo")
    imagen_vehiculo = models.ImageField(upload_to='imagenes_vehiculos/', blank=True, null=True, verbose_name="Imagen del Vehículo")
    nombre_responsable = models.CharField(max_length=100, verbose_name="Nombre de quien sube")
    rango_responsable = models.CharField(max_length=20, choices=RANGO_CHOICES, verbose_name="Rango de quien sube")
    observacion_mantenimiento = models.TextField(blank=True, null=True, verbose_name="Observación de Mantenimiento")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Subida")

    def __str__(self):
        return f"{self.nombre_vehiculo} - Placa: {self.placa}"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['-fecha_subida']