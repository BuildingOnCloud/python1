print ("         Clase #3")
print ("    Calculadora basica")
print ("")
print ("Seleccione función:")
print ("")
print ("1: Suma")
print ("2: Resta")
print ("3: Multiplicación")
print ("4: División")
print ("")
print ("")
print ("")
opción = input ("Ingresar función: ")
numeral_1 = float(input("primer digito: "))
numeral_2 = float(input("segundo digito: "))
if opción == '1':
    total = numeral_1 + numeral_2
    print (f"  {numeral_1} + {numeral_2} = {total}")
elif opción == '2':
    total = numeral_1 - numeral_2
    print (f"  {numeral_1} - {numeral_2} = {total}")
elif opción == '3':
    total = numeral_1 * numeral_2
    print (f"  {numeral_1} * {numeral_2} = {total}")
elif opción == '4':
    if numeral_2 !=0:
        total = numeral_1 / numeral_2
        print (f"  {numeral_1} / {numeral_2} = {total}")
    else:
        print ("Error: no divisible por cero")
else:
    print("Error selección de opción")
    