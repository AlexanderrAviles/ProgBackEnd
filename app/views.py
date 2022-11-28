from django.shortcuts import render
from django.http import Http404
from app.models import Vehiculo

# Create your views here.


def index(request):
    return render(request, 'index.html')


def vehiculos(request):
    cantidad = request.session.get("carrito_cantidad", 0)
    carrito = request.session.get("carrito", [])

    vehiculos = Vehiculo.objects.all()
    return render(request, 'Vehiculos.html', {"vehiculos": vehiculos, "cantidad_carrito": cantidad, "carrito": carrito})


def agregarAlCarro(request, id):
    cantidad = request.session.get("cantidad_carrito", 0)
    request.session["cantidad_carrito"] = cantidad + 1

    request.session["carrito"] = [
        {id: id, "cantidad": 1}
    ]
    return vehiculos(request)


def sucursal(request):
    return render(request, 'Sucursal.html')


def nosotros(request):
    return render(request, 'Nosotros.html')


def carrito(request):
    vehiculo = Vehiculo.objects.all()
    return render(request, 'carrito.html', {'vehiculo': vehiculo})


def ver(request):
    vehiculo = Vehiculo.objects.all()
    return render(request, "mostrarPrueba.html", {'vehiculo': vehiculo})


def vistaVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    print(vehiculo)
    return render(request, "vistaVehiculo.html", {"vehiculo": vehiculo})
