from django.contrib import admin
from .models import Vehiculo, Transmision, TipoUsuario, Usuario, TipoVehiculo, Color, Cilindrada, Marca
# Register your models here.


class TipoVehiculoAdmin(admin.ModelAdmin):
    ordering = ['tipoVehiculo']


class VehiculoAdmin(admin.ModelAdmin):
    ordering = ['marcaVehiculo', 'color', 'precio', 'modeloVehiculo',
                'imagen', 'cilindrada', 'rendimiento', 'rendimiento', 'ficha']


class ColorAdmin(admin.ModelAdmin):
    ordering = ['colorVehiculo']


class TransmisionAdmin(admin.ModelAdmin):
    ordering = ['Transmision']


class MarcaAdmin(admin.ModelAdmin):
    ordering = ['marcaVehiculo']


class CilindradaAdmin(admin.ModelAdmin):
    ordering = ['cilindrada']


class TipoUsuarioAdmin(admin.ModelAdmin):
    ordering = ['nombre']


class UsuarioAdmin(admin.ModelAdmin):
    ordering = ['nombre',
                'apellido',
                'rut',
                'telefono',
                'correo',
                'contraseña',
                'estado',
                'tipoUsuario',
                'estado']


admin.site.register(TipoVehiculo, TipoVehiculoAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Transmision, TransmisionAdmin)
admin.site.register(Cilindrada, CilindradaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)
