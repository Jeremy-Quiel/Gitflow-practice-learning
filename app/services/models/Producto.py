class Producto:
    def __init__(self, nombre, precio, tipo, marca):
        self.__nombre = nombre
        self.__precio = precio
        self.__tipo = tipo
        self.__marca = marca

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio
    

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def tipo(self):
        return self.__tipo


    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def marca(self):
        return self.__marca
    

    @marca.setter
    def marca(self, marca):
        self.__nombrmarca = marca


    def __str__(self):
        to_str = f"Nombre: {self.__nombre}\n"
        to_str += f"Precio: {self.__precio}\n"
        to_str += f"Tipo: {self.__tipo}\n"
        to_str += f"Marca: {self.__marca}\n"

        return to_str
