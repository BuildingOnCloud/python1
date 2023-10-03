class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        return f"{self.año} {self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, color):
        super().__init__(marca, modelo, año)
        self.color = color

    def describir(self):
        return f"{self.año} {self.color} {self.marca} {self.modelo} (Coche)"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def describir(self):
        return f"{self.año} {self.marca} {self.modelo} ({self.tipo})"
