"""
##############################################################################
# Author:  Jesus Ruiz                                                        #
# Date:    June 02, 2023                                                     #
# Version: 1.0                                                               #
#                                                                            #
# Description:                                                               #
# This Python script check how many strong is a password. This is Class 4's  #
# Exercise solution.                                                         #
#                                                                            #
# Requirements:                                                              #
# - Python 3.7+                                                              #
#                                                                            #
# Usage:                                                                     #
# - python3 clave_fuerte.py                                                  #
# - Input password.                                                          #
# - Apply rules over password and report how stronger it's.                  # 
#                                                                            #
# Disclaimer:                                                                #
# This code is provided as-is, without any warranties or guarantees. Use it  #
# at your own risk and review, test, and modify it according to your project #
# requirements and coding standards.                                         #
#                                                                            #
##############################################################################
"""

# Solicitar al usuario que ingrese una contraseña
contrasena = input("Por favor, ingrese una contraseña: ")

# Inicializar variables para verificar las reglas
longitud_suficiente = len(contrasena) >= 8
contiene_mayuscula = any(c.isupper() for c in contrasena)
contiene_minuscula = any(c.islower() for c in contrasena)
contiene_numero = any(c.isdigit() for c in contrasena)
contiene_caracter_especial = any(c in "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,." for c in contrasena)

# Verificar las reglas de seguridad
if (longitud_suficiente and contiene_mayuscula and contiene_minuscula and contiene_numero and contiene_caracter_especial):
    print("La contraseña es segura y cumple con todas las reglas.")
else:
    print("La contraseña no es segura. Debe cumplir con las siguientes reglas:")
    if not longitud_suficiente:
        print("- Tener al menos 8 caracteres de longitud.")
    if not contiene_mayuscula:
        print("- Contener al menos una letra mayúscula.")
    if not contiene_minuscula:
        print("- Contener al menos una letra minúscula.")
    if not contiene_numero:
        print("- Contener al menos un número.")
    if not contiene_caracter_especial:
        print("- Contener al menos un carácter especial.")
