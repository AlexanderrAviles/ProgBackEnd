from django.shortcuts import render, redirect
from django.http import Http404
from app.models import Vehiculo, Detalle, TipoUsuario, Transmision, TipoVehiculo, Color, Marca, Cilindrada
from app.carrito import Carrito
from datetime import datetime
from django.contrib.auth.models import User
from app import models
from app import forms
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    vehiculo = Vehiculo.objects.all()
    return render(request, 'index.html', {"vehiculo": vehiculo})


def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'Vehiculos.html', {"vehiculos": vehiculos})


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


def menuadmin(request):

    return render(request, "menuadmin.html")


def admintipovehiculo(request):
    return render(request, "admintipoVehiculo.html")


def admincolorvehiculo(request):
    return render(request, "admincolorVehiculo.html")


def adminmarcavehiculo(request):
    return render(request, "adminmarcaVehiculo.html")


def admincilindvehiculo(request):
    return render(request, "admincilindVehiculo.html")


def adminvehiculo(request):
    if request.method == "POST":
        vehiculo = Vehiculo()
        vehiculo.modeloVehiculo = request.POST["modelo"]
        vehiculo.precio = request.POST["precio"]
        vehiculo.cantidad = request.POST["cantidad"]
        vehiculo.imagen = request.FILES.get('imagen')
        tipoVehi = TipoVehiculo.objects.get(id=request.POST["tipovehiculo"])
        colorVehi = Color.objects.get(id=request.POST["colorvehiculo"])
        marcaVehi = Marca.objects.get(id=request.POST["marcavehiculo"])
        cilindVehi = Cilindrada.objects.get(id=request.POST["cilvehiculo"])
        traVehi = Transmision.objects.get(id=request.POST["travehiculo"])
        vehiculo.tipovehiculo = tipoVehi
        vehiculo.color = colorVehi
        vehiculo.marcaVehiculo = marcaVehi
        vehiculo.cilindrada = cilindVehi
        vehiculo.transmision = traVehi
        vehiculo.save()
        return redirect("admv")
    vehiculo = Vehiculo.objects.all()
    tipovehiculo = TipoVehiculo.objects.all()
    color = Color.objects.all()
    marca = Marca.objects.all()
    cilindrada = Cilindrada.objects.all()
    transmision = Transmision.objects.all()
    return render(request, "adminVehiculo.html", {"vehiculo": vehiculo, "tipovehiculo": tipovehiculo, "transmision": transmision, "color": color,
                                                  "marca": marca,
                                                  "cilindrada": cilindrada})


def editarvehiculo(request, idvehiculo):
    if request.method == 'POST':
        tipoVehi = TipoVehiculo.objects.get(id=request.POST["tipovehiculo"])
        colorVehi = Color.objects.get(id=request.POST["colorvehiculo"])
        marcaVehi = Marca.objects.get(id=request.POST["marcavehiculo"])
        traVehi = Transmision.objects.get(id=request.POST["travehiculo"])

        cilindVehi = Cilindrada.objects.get(id=request.POST["cilvehiculo"])
        print(traVehi)
        vehiculo = Vehiculo(idvehiculo, marcaVehi, colorVehi, tipoVehi, request.POST["precio"],
                            request.POST["modelo"], request.FILES.get(
            "imagen"), cilindVehi,
            request.POST["rendimiento"],
            request.FILES.get(
            "pdf"),
            request.FILES.get("imagen2"),
            request.FILES.get(
            "imagen3"), request.FILES.get("imagen4"),
            request.POST["desctitulo"], request.POST["desc"],
            request.POST["desctitulo1"], request.POST["desc1"],
            request.POST["desctitulo2"], request.POST["desc2"],
            request.POST["cantidad"], traVehi)

        vehiculo.save()

        return redirect("admv")
    else:
        vehiculo = Vehiculo.objects.get(id=idvehiculo)
        tipovehiculo = TipoVehiculo.objects.all()
        color = Color.objects.all()
        marca = Marca.objects.all()
        cilindrada = Cilindrada.objects.all()
        transmision = Transmision.objects.all()

        return render(request, "adminVehiculoeditar.html", {"vehiculo": vehiculo, "tipovehiculo": tipovehiculo, "color": color,
                                                            "marca": marca, "transmision": transmision,
                                                            "cilindrada": cilindrada})


def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()

    return redirect("admv")
#  login y registro
# rut contraseña


def indexlogin(request):
    return render(request, 'indexlogin.html')


def nosotroslogin(request):
    return render(request, 'nosotroslogin.html')


def sucursallogin(request):
    return render(request, 'sucursallogin.html')


def vehiculoslogin(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'Vehiculoslogin.html', {"vehiculos": vehiculos})


def vistavehiculologin(request):
    return render(request, 'vistaVehiculologin.html')


def verlogin(request):
    return render(request, 'mostrarPruebalogin.html')


def login(request):
    form = forms.IniciarSesion()
    if request.method == 'POST':
        form = forms.IniciarSesion(request.POST)
        rut = form['rut'].value()
        contraseña = form['contraseña'].value()
        user = auth.authenticate(username=rut, password=contraseña)
        if user is not None and user.is_active:
            print(rut)
            auth.login(request, user)
            # Redirect to a success page.
            print(user)

            # if user.username == 'Admin':
            #    return redirect('menuadmin')
            # elif user.username == 'Usuario':
            #    return redirect('indexLogin')
            # else:
            #    return HttpResponseRedirect(reverse('index'))
            # if user.tipoUsuario.nombre == 'usuario':
            #     return redirect('indexlogin')
            # elif user.tipoUsuario.nombre == 'admin':
            #     return redirect('menuadmin')
            # else:
            #     return HttpResponseRedirect(reverse('index'))
            return redirect('indexlogin')
        else:
            print("no entro")
            return redirect('login')
    tp = TipoUsuario.objects.all()
    datos = {'form': form,'tp':tp}
  
    return render(request, 'login.html', datos)


def crearUsuario(formulario):
    usuario = models.Usuario()
    usuario.nombre = formulario.cleaned_data['nombre']
    usuario.apellido = formulario.cleaned_data['apellido']
    usuario.rut = formulario.cleaned_data['rut']
    usuario.telefono = formulario.cleaned_data['telefono']
    usuario.correo = formulario.cleaned_data['correo']
    usuario.contraseña = formulario.cleaned_data['contraseña']
    usuario.terminos = formulario.cleaned_data['terminos']
    usuario.estado = True

    user = User.objects.create_user(username=usuario.rut, email=usuario.correo, password=usuario.contraseña,
                                    first_name=usuario.nombre, last_name=usuario.apellido, is_staff=False, is_active=True, is_superuser=False)
    user.save()
    usuario.save()


def registro(request):
    form = forms.userRegistrationForm()
    if request.method == 'POST':
        form = forms.userRegistrationForm(request.POST)
        if form.is_valid():
            if models.Usuario.objects.filter(rut__icontains=form.cleaned_data['rut']).__len__() == 0:
                crearUsuario(form)
                return redirect('login')
            else:
                print("Correo ingresado ya se encuentra registrado")
                data = {'form': form}
                return render(request, 'registro.html', data)
    data = {'form': form}
    return render(request, 'registro.html', data)
