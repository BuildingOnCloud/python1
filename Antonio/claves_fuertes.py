#Claves Fuertes

#Escriba un programa tn Python que solicite al usuario ingresar
#una contraseña y luego evalue su seguridad utilizando las siguientes reglas:

#1. la Contrasena debe tener por lo menos 8 caracteres
#2. Debe contener al menos una letra mayuscula y al menos una minuscula
#3. Debe contener un numero
#4. Debe contener al menor un caracter especial: !, #, @, $, %, etc.

clave = input("Ingrese una contraseña:")
longitud = len(clave)
#regla 1
if longitud <= 8:
    print("- Debe tener por los menos 8 dígitos.\n")
#regla 2
contiene_mayuscula = False
for c in clave:
    if c.isupper():
        contiene_mayuscula = True
        break
if not contiene_mayuscula:
    print("- Debe contener por lo menos una mayúscula.\n")
#regla 3
contiene_minuscula = False
for c in clave:
    if c.islower():
        contiene_minuscula = True
        break
if not contiene_minuscula:
    print("- Debe contener por lo menos una minúscula.\n")
#regla 4
contiene_numero = False
for c in clave:
    if c.isdigit():
        contiene_numero = True
        break
if not contiene_numero:
    print("- Debe contener por lo menos un número.\n")
#regla 5
contiene_sc = any(c in "!#$%&'()*+,-./:;<=>?@[\]^_`{|} ~." for c in clave)
if not contiene_sc:
    print("- Debe contener por lo menos un caracter especial")

if (
    longitud
    and contiene_mayuscula
    and contiene_minuscula
    and contiene_numero
    and contiene_sc
):
    print("La contraseña es segura")