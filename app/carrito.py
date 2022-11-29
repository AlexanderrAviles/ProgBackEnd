class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, vehiculo):
        id = str(vehiculo.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "vehiculo_id": vehiculo.id,
                "modeloVehiculo": vehiculo.modeloVehiculo,
                "marcaVehiculo": vehiculo.marcaVehiculo.marcaVehiculo,
                "cantidad": 1,
                "precio": vehiculo.precio,
                "imagen": vehiculo.imagen.url,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += vehiculo.precio

        self.guardar()

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, vehiculo):
        vehiculo_id = str(vehiculo.id)
        if vehiculo_id in self.carrito:
            del self.carrito[vehiculo_id]
            self.guardar()

    def restar(self, vehiculo):
        id = str(vehiculo.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] -= vehiculo.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(vehiculo)
            self.guardar()

    def disminuir(self, vehiculo):
        for key, value in self.carrito.items():
            if key == str(vehiculo.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.eliminar(vehiculo)
                break
            else:
                print("El vehiculo no existe en el carrito")

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
