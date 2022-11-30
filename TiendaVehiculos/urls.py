from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views as v
from django.contrib.auth.views import logout_then_login

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
    path('carrito/eliminar/<int:vehiculo_id>/',
         v.eliminarCarro, name="eliminar"),
    path('carrito/restar/<int:vehiculo_id>/', v.restarCarro, name="restar"),
    path('carrito/limpiar/', v.limpiarCarro, name="Clean"),
    path('carrito/ingresarPedido/', v.ingresarPedido, name="ingresarPedido"),

    path('menuadmin/', v.menuadmin, name='mnadm'),
    path('admintv/', v.admintipovehiculo, name='admtv'),
    path('admincv/', v.admincolorvehiculo, name='admcv'),
    path('adminmv/', v.adminmarcavehiculo, name='admmv'),
    path('adminclv/', v.admincilindvehiculo, name='admclv'),
    path('adminv/', v.adminvehiculo, name='admv'),
    path('adminveditar/<int:idvehiculo>', v.editarvehiculo, name='admvedi'),
    path('adminveliminar/<int:id>', v.eliminarVehiculo, name='admvdel'),
    # login registro
    path('indexl/', v.indexlogin, name='indexlogin'),
    path('accounts/login/', v.login, name='login'),
    path('registro/', v.registro, name='registro'),
    path('logout/', logout_then_login, name='logout'),
    path('vehiculosl/', v.vehiculoslogin, name='vehiculoslogin'),
    path('sucursall/', v.sucursallogin, name='sucursallogin'),
    path('nosotrosl/', v.nosotroslogin, name='nosotroslogin'),
    path('vistaVehiculo/<int:id>', v.vistavehiculologin, name='vistaVehiculologin'),
    path('verl/', v.verlogin, name='verlogin')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
