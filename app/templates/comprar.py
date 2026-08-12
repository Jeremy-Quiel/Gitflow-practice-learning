def comprar():
    while True:
        print("="*20)

        print("futura lista de datos")

        print("="*20)

        print("(0) salir al menu principal")
        print("(number id) comprar producto seleccionado")

        print("="*20)

        opc = int(input("Seleccione el producto por el ID para comprar: "))

        if opc == 0:
            break

