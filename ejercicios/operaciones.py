"""
##############################################################################
# Author:  Jesus Ruiz                                                        #
# Date:    June 05, 2023                                                     #
# Version: 1.0                                                               #
#                                                                            #
# Description:                                                               #
# This Python module contains basic operations used on calculator app        #
#                                                                            #
# Requirements:                                                              #
# - Python 3.7+                                                              #
#                                                                            #
# Usage:                                                                     #
# - import operaciones                                                       #
#                                                                            #
# Disclaimer:                                                                #
# This code is provided as-is, without any warranties or guarantees. Use it  #
# at your own risk and review, test, and modify it according to your project #
# requirements and coding standards.                                         #
#                                                                            #
##############################################################################
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("¡No se puede dividir por cero!")
    return a / b
