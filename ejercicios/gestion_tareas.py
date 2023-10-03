"""
##############################################################################
# Author:  Jesus Ruiz                                                        #
# Date:    June 03, 2023                                                     #
# Version: 1.0                                                               #
#                                                                            #
# Description:                                                               #
# This Python app act like a Task Manager, add tasks, list and mark as       #
# completed tasks and delete task                                            #
#                                                                            #
# Requirements:                                                              #
# - Python 3.7+                                                              #
#                                                                            #
# Usage:                                                                     #
# - python3 gestion_tareas.py                                                #
# - Input operations and apply them over tasks                               #
#                                                                            #
# Disclaimer:                                                                #
# This code is provided as-is, without any warranties or guarantees. Use it  #
# at your own risk and review, test, and modify it according to your project #
# requirements and coding standards.                                         #
#                                                                            #
##############################################################################
"""
# Creamos la lista de la tareas
lista_tareas = []

# Ciclamos mientras mientras el usuario no eliga Salir
while True:
    print("\nGestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = input("Selecciona una opción (1/2/3/4/5): ")

    if opcion == "1": # Agregar Tarea

        tarea = input("Ingresa la tarea: ")
        if tarea == '':
            print("Ingreso de Tarea invalido.")
        else: 
            lista_tareas.append(tarea)
            print(f"Tarea '{tarea}' agregada con éxito.")

    elif opcion == "2":  # Ver Tareas

        if not lista_tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(lista_tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == "3": # Marcar Tarea Completada

        if not lista_tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(lista_tareas, start=1):
                print(f"{i}. {tarea}")

            numero_tarea = int(input("Ingresa el número de la tarea completada: "))

            if 1 <= numero_tarea <= len(lista_tareas):
                tarea_completada = lista_tareas.pop(numero_tarea - 1)
                print(f"Tarea '{tarea_completada}' marcada como completada.")
            else:
                print("Número de tarea no válido.")

    elif opcion == "4": # Eliminar Tarea

        if not lista_tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(lista_tareas, start=1):
                print(f"{i}. {tarea}")

            numero_tarea = int(input("Ingresa el número de la tarea a eliminar: "))

            if 1 <= numero_tarea <= len(lista_tareas):
                tarea_eliminada = lista_tareas.pop(numero_tarea - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Número de tarea no válido.")

    elif opcion == "5": # Salir

        print("¡Hasta luego!")
        break

    else:   # Opcion de Menu No Valida

        print("Opción no válida. Por favor, selecciona una opción válida.")