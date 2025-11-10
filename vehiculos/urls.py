# urls.py (del app)
from django.urls import path
from . import views
app_name = 'vehiculos'
urlpatterns = [
    path('crear-vehiculo/', views.crear_vehiculo, name='crear_vehiculo'),
    path('lista-vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('editar-vehiculo/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar-vehiculo/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]