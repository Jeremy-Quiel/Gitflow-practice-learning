import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.models.Producto import Producto

class Conn:
    def __init__(self):
        self.__productos = [Producto("Procesador", 1500, "Componente", "Intel"), Producto("Tarjeta Grafica", 2750, "Componente", "AMD")]

    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, productos):
        self.__productos = productos

    def add(self, producto):
        self.__productos.append(producto)

    def delete(self, producto):
        self.__productos.remove(producto)

    def search(self, id):
        for producto in self.__productos:
            if producto.id == id:
                return Producto
            
        return None