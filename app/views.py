from django.shortcuts import render, redirect
from django.http import Http404
from app.models import Vehiculo, Detalle
from app.carrito import Carrito
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'Vehiculos.html', {"vehiculos": vehiculos})


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

    # agregar productos al carro


def agregarCarro(request, vehiculo_id):
    carrito = Carrito(request)
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    print(vehiculo)
    carrito.agregar(vehiculo)
    return redirect("carrito")

# eliminar el carro


def eliminarCarro(request, vehiculo_id):
    carrito = Carrito(request)
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    carrito.eliminar(vehiculo)
    return redirect("carrito")

# restar productos al carro


def restarCarro(request, vehiculo_id):
    carrito = Carrito(request)
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    carrito.restar(vehiculo)
    return redirect("carrito")

# limpiar productos del carro


def limpiarCarro(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")


def back(request):
    return redirect("vehiculos")


def ingresarPedido(request):
    if request.method == 'POST':
        detPed = Detalle()
        detPed.fecha_pedido = datetime.now()
        print(request.POST.get("prePed"))
        detPed.precio_total = int((request.POST.get('prePed')))
        detPed.save()

        return redirect("index")

    vehiculos = Vehiculo.objects.all()
    return render(request, "vehiculos.html", {"vehiculos": vehiculos})
