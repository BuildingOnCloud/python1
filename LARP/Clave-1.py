while True:
        largo = False
        minuscula = False
        mayuscula = False
        numero = False
        car_especial = False
        validacion = []

        clave = input('Ingrese una contraseña para acceder, o deje vacío para finalizar: ')
  
        if len(clave) == 0:
            print('Programa finalizado')
            break
        if len(clave) >= 8:
            largo = True
            validacion.append(largo)

        for l in clave:
            if l.islower() and not minuscula:
                minuscula = True
                validacion.append(minuscula)
            if l.isupper() and not mayuscula:
                mayuscula = True
                validacion.append(mayuscula)
            if l.isdigit() and not numero:
                numero = True
                validacion.append(numero)
            if not l.isalnum() and not car_especial:
                car_especial = True
                validacion.append(car_especial)

            if minuscula and mayuscula and numero and car_especial:
                break

        if len(validacion) == 5:
            print('<<<<< ACCESO PERMITIDO >>>> ')
            break
        else:
            print(f'<<<<< ACCESO DENEGADO >>>> ESTA CONTRASEÑA :  {clave}   NO CUMPLE LOS REQUISITOS, SIGUE LAS INSTRUCCIONES:')
            print("""
Requisitos para la contraseña:
    1. La contraseña debe tener al menos 8 caracteres de longitud.
    2. Debe contener al menos una letra mayúscula y al menos una letra minúscula.
    3. Debe contener al menos un número.
    4. Debe contener al menos un carácter especial, como !, @, #, $, %, etc.
        """)