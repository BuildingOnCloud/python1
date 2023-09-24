print("Calculadora")

n1 = float(input("Ingresar un numero cualquiera"))
n2 = float(input("Ingresar un numero cualquiera"))
x = True
while(x == True):
    print("Para sumar los dos numeros ingresados, ingrese 1")
    print("Para restar los dos numeros ingresados, ingrese 2")
    print("Para multiplicar los dos numeros ingresados, ingrese 3")
    print("Para dividir los dos numeros ingresados, ingrese 4")
    print("Para salir, ingrese 0")
    op = int(input("Ingresa el numero segun la operacion que se quiera realizar"))

    if op ==  1:
        print("\n\n\n<---------------Suma----------------->\n\n\n")
        print(f"\n\n\nEl resultado de la suma es: ${n1+n2}\n\n\n")
        print("\n\n\n<---------------Suma----------------->\n\n\n")
    elif op == 2:
        print("\n\n\n<---------------Resta----------------->\n\n\n")
        print(f"\n\n\nEl resultado de la resta es: ${n1-n2}\n\n\n")
        print("\n\n\n<---------------Resta----------------->\n\n\n")
    elif op == 3:
        print("\n\n\n<---------------Multiplicacion----------------->\n\n\n")
        print(f"\n\n\nEl resultado de la multiplicacion es: ${n1*n2}\n\n\n")
        print("\n\n\n<---------------Multiplicacion----------------->\n\n\n")
    elif (op == 4):
        print("\n\n\n<---------------Division----------------->\n\n\n")
        print(f"\n\n\nEl resultado de la division es: ${n1/n2}\n\n\n")
        print("\n\n\n<---------------Division----------------->\n\n\n")
    else:
        x = False





