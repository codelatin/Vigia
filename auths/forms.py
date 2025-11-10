from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# --------------------------
# FORMULARIO DE REGISTRO
# --------------------------
class RegistroForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nombres",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese sus nombres'
        })
    )
    last_name = forms.CharField(
        label="Apellidos",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese sus apellidos'
        })
    )
    email = forms.EmailField(
        label="Correo electrónico institucional",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'usuario@ejercito.mil.co'
        })
    )

    # Campos personalizados militares
    document_id = forms.CharField(
        label="Documento de identidad",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1234567890'})
    )
    phone = forms.CharField(
        label="Teléfono de contacto",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3001234567'})
    )
    military_id = forms.CharField(
        label="ID Militar",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código militar'})
    )
    rank = forms.ChoiceField(
        label="Rango / Grado",
        choices=[
            ('soldado', 'Soldado Profesional'),
            ('cabo', 'Cabo'),
            ('suboficial', 'Suboficial'),
            ('sargento', 'Sargento'),
            ('tecnico', 'Técnico de Mantenimiento'),
            ('supervisor', 'Supervisor'),
            ('jefe', 'Jefe de Unidad'),
            ('comandante', 'Comandante'),
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    unit = forms.CharField(
        label="Unidad Militar",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Compañía Junín'})
    )
    specialty = forms.ChoiceField(
        label="Especialidad / Área",
        choices=[
            ('mecanica', 'Mecánica Automotriz'),
            ('electrica', 'Sistemas Eléctricos'),
            ('operador', 'Operador de Vehículos'),
            ('logistica', 'Logística y Abastecimiento'),
            ('administracion', 'Administración'),
            ('otro', 'Otro'),
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    experience = forms.CharField(
        label="Años de experiencia",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Años de experiencia'})
    )
    role = forms.ChoiceField(
        label="Rol Solicitado",
        choices=[
            ('operador', 'Operador'),
            ('tecnico', 'Técnico'),
            ('supervisor', 'Supervisor'),
            ('admin', 'Administrador'),
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    justification = forms.CharField(
        label="Justificación del acceso",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        # Genera un username automáticamente basado en el email
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# --------------------------
# FORMULARIO DE LOGIN
# --------------------------
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        })
    )
