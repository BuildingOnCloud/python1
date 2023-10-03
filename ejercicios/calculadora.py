"""
##############################################################################
# Author:  Jesus Ruiz                                                        #
# Date:    June 01, 2023                                                     #
# Version: 1.0                                                               #
#                                                                            #
# Description:                                                               #
# This Python script create a simple calculator with basic arithmetic        #
# operations like add, substraction, multiplication and division. This is    #
# Class 3's Exercise solution.                                               #
#                                                                            #
# Requirements:                                                              #
# - Python 3.7+                                                              #
#                                                                            #
# Usage:                                                                     #
# - python3 calculadora.py                                                   #
# - Input first operand number.                                              #
# - Input second operand number.                                             #
# - Choose wich operations do you need                                       #
# - Result will be print it.                                                 # 
#                                                                            #
# Disclaimer:                                                                #
# This code is provided as-is, without any warranties or guarantees. Use it  #
# at your own risk and review, test, and modify it according to your project #
# requirements and coding standards.                                         #
#                                                                            #
##############################################################################
"""

# Solicita al usuario que ingrese dos numeros operandos
numero1 = float(input("Ingrese primer número: "))
numero2 = float(input("Ingrese segundo número: "))

# Muestra el menú de operaciones
print("\nSeleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicita al usuario que elija una operación
opcion = input("Ingrese el número de la operación deseada: ")

# Realiza la operación seleccionada y muestra el resultado
if opcion == '1':
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == '2':
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == '3':
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor, seleccione una opción válida (1, 2, 3 o 4).")