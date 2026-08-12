from private.app.templates.comprar import comprar
from private.app.templates.vender import vender

while True:
    print(f"="*20)

    print(f"Tienda de JarTech")
    print(f"(1) Comprar Productos")
    print(f"(2) Vender Productos")
    print(f"(0) Salir de la app")
    print(f"="*20)

    opc = int(input("Opcion: "))

    if opc == 0:
        break

    if opc == 1:
        comprar()
        continue

    if opc == 2:
        vender()
        continue

