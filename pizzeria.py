Bienvenidos a Pizzas Karyto.

Pizzas = ["Pepperoni", "Queso", "Margherita", "Napolitana"]

 def imprimir_menu ()
        imprimir("1 mostrar pizzas")
        imprimir("2 eliminar pizzas")
        imprimir("3 agregar pizzas")
        imprimir("4 salir")
        valor = input("Ingrese el valor de la accion: ")
        return valor
continuar = true

while continuar:
    # v_retornado = Valor Retornado
    v_retornado = imprimir_menu()
    if int(v_retornado) == 1:
            for pizza in pizzas:
                print(pizza)
    elsif int(v_retornado) == 2:
            pizzas = []
    elsif int(v_retornado) == 3:
            valor = input ("Ingrese las pizzas a agregar")
            productos.append(valor)
    elsif int(v_retornado) == 4:
            continuar = false
    else:
        print("opcion no controlada")
