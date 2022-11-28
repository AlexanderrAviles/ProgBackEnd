from django.contrib import admin
from .models import Vehiculo,TipoVehiculo,Color,Cilindrada,Marca
# Register your models here.


class TipoVehiculoAdmin(admin.ModelAdmin):
    ordering = ['tipoVehiculo']
    
class VehiculoAdmin(admin.ModelAdmin):
    ordering = ['marcaVehiculo','color','precio','modeloVehiculo','imagen','cilindrada','rendimiento','transmision','ficha']

class ColorAdmin(admin.ModelAdmin):
    ordering = ['colorVehiculo']
    
class MarcaAdmin(admin.ModelAdmin):
    ordering = ['marcaVehiculo']
    
class CilindradaAdmin(admin.ModelAdmin):
    ordering = ['cilindrada']

admin.site.register(TipoVehiculo, TipoVehiculoAdmin)
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Cilindrada, CilindradaAdmin)
admin.site.register(Marca, MarcaAdmin)
