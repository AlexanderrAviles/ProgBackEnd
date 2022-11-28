from django.db import models

# Create your models here.


class Marca(models.Model):
    marcaVehiculo = models.CharField(max_length=30)

    def __str__(self):
        return self.marcaVehiculo


class Color(models.Model):
    colorVehiculo = models.CharField(max_length=30)

    def __str__(self):
        return self.colorVehiculo


class TipoVehiculo(models.Model):
    tipoVehiculo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipoVehiculo


class Cilindrada(models.Model):
    cilindrada = models.IntegerField()

    def __str__(self):
        return str(self.cilindrada)


class Vehiculo(models.Model):
    marcaVehiculo = models.ForeignKey(Marca, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    tipovehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    precio = models.IntegerField()
    modeloVehiculo = models.CharField(max_length=30)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    cilindrada = models.ForeignKey(Cilindrada, on_delete=models.CASCADE)
    rendimiento = models.CharField(max_length=30)
    transmision = models.CharField(max_length=30)
    ficha = models.FileField(null=True)
    imagen2 = models.ImageField(null=True, blank=True, upload_to="images/")
    imagen3 = models.ImageField(null=True, blank=True, upload_to="images/")
    imagen4 = models.ImageField(null=True, blank=True, upload_to="images/")
    desctitulo = models.CharField(max_length=100)
    desc = models.CharField(max_length=2000)
    desctitulo1 = models.CharField(max_length=100)
    desc1 = models.CharField(max_length=2000)
    desctitulo2 = models.CharField(max_length=100)
    desc2 = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.modeloVehiculo)
