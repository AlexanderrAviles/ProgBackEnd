from django.db import models

# Create your models here.

class Marca(models.Model):
    marcaVehiculo= models.CharField(max_length=30)
    
class Color(models.Model):
    colorVehiculo= models.CharField(max_length=30)
    
class TipoVehiculo(models.Model):
    tipoVehiculo= models.CharField(max_length=30)

class Vehiculo(models.Model):
    marcaVehiculo=models.ForeignKey(Marca, on_delete=models.CASCADE)
    color=models.ForeignKey(Color, on_delete=models.CASCADE)
    tipovehiculo= models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    precio=models.IntegerField(30)
    modeloVehiculo=models.CharField(max_length=30)
    Cantidad=models.IntegerField()
    url_imagen=models