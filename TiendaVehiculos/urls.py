from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='index'),
    path('vehiculos/', v.vehiculos, name='vehiculos'),
    path('sucursal/', v.sucursal, name='sucursal'),
    path('nosotros/', v.nosotros, name='nosotros'),
    path('vehiculoSelect/', v.vehiculoSelect, name='vehiculoSelect'),
    path('vistaVehiculo/', v.vistaVehiculo, name='vistaVehiculo'),
    path('ver/', v.ver, name='ver'),
    path('carrito/<int:id>', v.agregarAlCarro),
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
