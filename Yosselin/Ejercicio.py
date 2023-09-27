print("\nGestión de tareas")
print("1. Agregar")
print("2. Ver tareas pendientes")
print("3. Marcar tarea completada")
print("4. Eliminar tarea")
print("5. Salir del programa")

lista = []

while True:
    opcion = input("Ingrese un número del 1 al 5: ")

    if opcion == '1':
        tarea = input("Agregar tarea: ")
        lista.append(tarea)
        
    elif opcion == '2':
        print("Tareas pendientes:")
        for i, tarea in enumerate(lista, 1):
            print(f"{i}. {tarea}")
            
    elif opcion == '3':
        for i, tarea in enumerate(lista, 1):
            print(f"{i}. {tarea}")
        comple = int(input ("Ingrese número de la tarea completada: "))
        if 1<= comple <=len(lista):
            tareaC= lista[comple-1]
            del lista[comple-1]
            print(f"Se marcó como tarea completada: {tareaC}")
        else:
            print("Tarea no encontrada")

    
    elif opcion == '4':
        for i, tarea in enumerate(lista, 1):
            print(f"{i}. {tarea}")  
        elimina = input("Ingrese numero de la tarea a eliminar ")
        elimina = int(elimina)
        if 1 <= elimina <= len(lista):
            tareaEliminada = lista[elimina - 1]
            lista.remove(tareaEliminada)
            
            print(f"Tarea eliminada: {tareaEliminada}")
        else:
            print("Número de tarea no válido.")
    
    elif opcion == '5':
        print("Hasta pronto.")
        break
    
    else:
        print("Error. Ingresar un número válido del 1 al 5.")
