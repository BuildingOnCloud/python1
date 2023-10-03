"""
##############################################################################
# Author:  Jesus Ruiz                                                        #
# Date:    June 04, 2023                                                     #
# Version: 1.0                                                               #
#                                                                            #
# Description:                                                               #
# This Python app act like a Temperature Tracker save several temperatures   #
# and make some statictics over this data                                    #
#                                                                            #
# Requirements:                                                              #
# - Python 3.7+                                                              #
#                                                                            #
# Usage:                                                                     #
# - python3 temperaturas.py                                                  #
# - Input dates and dates                                                    #
#                                                                            #
# Disclaimer:                                                                #
# This code is provided as-is, without any warranties or guarantees. Use it  #
# at your own risk and review, test, and modify it according to your project #
# requirements and coding standards.                                         #
#                                                                            #
##############################################################################
"""

# Función para calcular el promedio de temperaturas
def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        return 0
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función para encontrar la temperatura máxima
def encontrar_maxima(temperaturas):
    return max(temperaturas)

# Función para encontrar la temperatura mínima
def encontrar_minima(temperaturas):
    return min(temperaturas)

# Programa principal
registro_temperaturas = {}  # Usamos un diccionario para registrar temperaturas con fechas

while True:
    fecha = input("Ingresa la fecha (o 'fin' para terminar): ")
    
    if fecha.lower() == "fin":
        break
    
    try:
        temperatura = int(input("Ingresa una temperatura: "))
        
        if fecha in registro_temperaturas:
            registro_temperaturas[fecha].append(temperatura)
        else:
            registro_temperaturas[fecha] = [temperatura]
    except ValueError:
        print("Entrada no válida. Ingresa una fecha y una temperatura válida o 'fin' para terminar.")

if not registro_temperaturas:
    print("No se ingresaron temperaturas.")
else:
    for fecha, temperaturas in registro_temperaturas.items():
        promedio = calcular_promedio(temperaturas)
        maxima = encontrar_maxima(temperaturas)
        minima = encontrar_minima(temperaturas)
        
        print(f"Fecha: {fecha}")
        print(f"Temperatura: {temperaturas}")
        print(f"Temperatura Promedio: {promedio:.2f}")
        print(f"Temperatura Máxima: {maxima}")
        print(f"Temperatura Mínima: {minima}")
        print()

# Conversión del registro de temperaturas en un diccionario inmutable (tupla de tuplas)
registro_temperaturas = tuple((fecha, tuple(temperaturas)) for fecha, temperaturas in registro_temperaturas.items())

print(f"Registro de Temperaturas en una Tupla de Tuplas:\n{registro_temperaturas}")
