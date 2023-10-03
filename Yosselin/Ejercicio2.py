def promedioTemp(temperatura):
    if len(temperatura) == 0:
        return 0
    suma = sum(temperatura)
    promedio = suma / len(temperatura)
    return promedio

def tempMax(temperatura):
    return max(temperatura)

def tempMinima(temperatura):
    return min(temperatura)

registroTemperatura = {}
temperaturas = []

while True:
    fecha = input("Ingrese fecha o 'fin' para terminar: ")
    
    if fecha.lower() == "fin":
        break
    
    try:
        temperatura = int(input("Ingresar temperatura: "))
        temperaturas.append(temperatura)  # Agregar la temperatura a la lista
        
        if fecha in registroTemperatura:
            registroTemperatura[fecha].append(temperatura)
        else:
            registroTemperatura[fecha] = [temperatura]
    except ValueError:
        print("No válido")
        
if not temperaturas:
    print("No se ingresaron las temperaturas")
else:
    promedio_total = promedioTemp(temperaturas)
    maxima_total = tempMax(temperaturas)
    minima_total = tempMinima(temperaturas)
    
    print(f"Temperatura promedio de todas las temperaturas: {promedio_total:.2f}")
    print(f"Temperatura máxima de todas las temperaturas: {maxima_total}")
    print(f"Temperatura mínima de todas las temperaturas: {minima_total}")
    
if not registroTemperatura:
    print("No se ingresaron temperaturas por fecha")
else:
    registroTemperaturaTupla = tuple((fecha, tuple(temperatura)) for fecha, temperatura in registroTemperatura.items())
    print(f"Registro de Temperaturas por Fecha en una Tupla de Tuplas: \n{registroTemperaturaTupla}")
