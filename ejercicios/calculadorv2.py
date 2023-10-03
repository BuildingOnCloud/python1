"""
##############################################################################
# Author:  Jesus Ruiz                                                        #
# Date:    June 05, 2023                                                     #
# Version: 1.0                                                               #
#                                                                            #
# Description:                                                               #
# This Python app is a calculator with use of modules.                       #
#                                                                            #
# Requirements:                                                              #
# - Python 3.7+                                                              #
#                                                                            #
# Usage:                                                                     #
# - python3 calculadorv2.py                                                  #
# - Input numbers and operations                                             #
#                                                                            #
# Disclaimer:                                                                #
# This code is provided as-is, without any warranties or guarantees. Use it  #
# at your own risk and review, test, and modify it according to your project #
# requirements and coding standards.                                         #
#                                                                            #
##############################################################################
"""

from operaciones import suma, resta, multiplicacion, division

while True:
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Selecciona una operación (1/2/3/4/5): ")

    if opcion == "5":
        break
    
    if opcion not in ("1", "2", "3", "4"):
        print("Opción no válida. Ingresa un número del 1 al 4.")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = suma(num1, num2)
        elif opcion == "2":
            resultado = resta(num1, num2)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
        elif opcion == "4":
            resultado = division(num1, num2)

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingresa números válidos.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
