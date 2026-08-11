class Producto:
    def __init__(self, nombre, precio, tipo, marca):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.marca = marca

    def __str__(self):
        to_str = f"Nombre: {self.nombre}\n"
        to_str += f"Precio: {self.precio}\n"
        to_str += f"Tipo: {self.tipo}\n"
        to_str += f"Marca: {self.marca}\n"

        return to_str