from pickletools import read_uint1
def suma (n1, n2):
    return n1 + n2
def resta (n1, n2):
    return n1 - n2
def multi (n1, n2):
    return n1 * n2
def divi (n1, n2):
    if n2 == 0:
        return "No se leso dividir entre 0 no se llama"
    return n1 / n2
def calculadora():
    print("            ***** Seleccione una operacion :*****           ")
    print("1. ---------------------<Suma>------------------------------")
    print("2. ---------------------<Resta>-----------------------------")
    print("3. ---------------------<Multiplicacion>--------------------")
    print("4. ---------------------<Division>--------------------------")
    opcion = int(input("Ingrese el numero de la operacion deseada: "))
    n1 = float(input("Ingrese el primer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))
    
    if opcion == 1:
        print("Resultado:", suma(n1, n2))
    elif opcion == 2:
        print("Resultado:", resta(n1, n2))
    elif opcion == 3:
        print("Resultado:", multi(n1, n2))
    elif opcion == 4:
        print("Resultado:", divi(n1, n2))
    else:
        print("Opcion no valida")
calculadora ()