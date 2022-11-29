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
    path('vistaVehiculo/<int:id>', v.vistaVehiculo, name='vistaVehiculo'),
    path('ver/', v.ver, name='ver'),
    path('carrito/', v.carrito, name="carrito"),
    path('carrito/<int:vehiculo_id>/', v.agregarCarro, name="agregar"),
    path('carrito/eliminar/<int:vehiculo_id>/', v.eliminarCarro, name="eliminar"),
    path('carrito/restar/<int:vehiculo_id>/', v.restarCarro, name="restar"),
    path('carrito/limpiar/', v.limpiarCarro, name="Clean"),
    path('carrito/ingresarPedido/', v.ingresarPedido, name="ingresarPedido"),

    path('adminlogin/', v.adminlogin, name='admlogin'),
    path('menuadmin/', v.menuadmin, name='mnadm'),
    path('admintv/', v.admintipovehiculo, name='admtv'),
    path('admincv/', v.admincolorvehiculo, name='admcv'),
    path('adminmv/', v.adminmarcavehiculo, name='admmv'),
    path('adminclv/', v.admincilindvehiculo, name='admclv'),
    path('adminv/', v.adminvehiculo, name='admv'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
