class Producto:
    def __init__(self, nombre, precio, tipo, marca):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.marca = marca

    @property
    def nombre(self):
        return self.nombre
    

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def precio(self):
        return self.precio
    

    @precio.setter
    def precio(self, precio):
        self.precio = precio

    @property
    def tipo(self):
        return self.tipo


    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo

    @property
    def marca(self):
        return self.marca
    

    @marca.setter
    def marca(self, marca):
        self.nombrmarca = marca
