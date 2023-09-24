#clase 4:(CLON)
 
#Indicar condiciones en cadena por cumplimiento de parametro al crear clave

# condiciones:
# 1 La contraseña debe tener al menos 8 caracteres de longitud.
# 2. Debe contener al menos una letra mayúscula y al menos una letra minúscula.
# 3. Debe contener al menos un número.
# 4. Debe contener al menos un carácter especial, como !, @, #, $, %, etc

print ("\tclase 4:\n     crear clave\n")
print ("Su clave debe cumplir con los siguientes parametros:\n\n1. Minimo 8 caracteres\n2. Contener almenos una letra mayuscula y minuscula\n3. Contener almenos 1 numeral\n4. Contener almenos 1 caracter especial:\n\t!#$%&/()=?¡[]{}-.,_")
clave = input ("\nIngrese clave:\n")
longitud = len(clave) >= 8
mayuscula = any(c.isupper() for c in clave)
minuscula = any(c.islower() for c in clave)
numeral = any(c.isdigit() for c in clave)
especial = any(c in "!#$%&/()=?¡[]{}-.,_" for c in clave)

print ("\n")
if (longitud and mayuscula and minuscula and numeral and especial):
    print("ok, clave cumple con condiciones")
else:
    print("Error, verificar condiciones:\n")
    if not longitud: 
        print ("menos de 8 caracteres")
    if not mayuscula:
        print("no contiente mayusculas")
    if not minuscula:
        print ("no contiene minusculas")
    if not numeral:
        print ("no contiene numeros")
    if not especial:
        print ("no contiene caracteres especiales: !#$%&/()=?¡[]{}-.,_")
    print ("\n")
