class Producto:
    def __init__(self, id, nombre, precio, tipo, marca):
        self.__id = id
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.marca = marca

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

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


    def __str__(self):
        to_str = f"Id: {self.__id}"
        to_str += f"Nombre: {self.nombre}\n"
        to_str += f"Precio: {self.precio}\n"
        to_str += f"Tipo: {self.tipo}\n"
        to_str += f"Marca: {self.marca}\n"

        return to_str
