print ("Calculadora Basica - Curso de Python")
number1=float(input("Ingrese primer numero:"))
number2=float(input("ingreso segundo numero:"))

Opcion = 0

while Opcion != 6:
     print("""
     Teclea tu opción:
           
     1. Suma
     2. Resta
     3. Multiplicación
     4. División
     5. Otros valores
     6. Salir                                             
     """)
     
     Opcion = int(input())

     if Opcion == 1:
          print(" ")
          print("Resultado:", number1,"+", number2,"=",number1+number2)

     if Opcion == 2:
          print(" ")
          print("Resultado:", number1,"-", number2,"=",number1-number2)

     if Opcion == 3:
          print(" ")
          print("Resultado:", number1,"*", number2,"=",number1*number2)

     if Opcion == 4:
          if number2 != 0:
               print(" ")
               print("Resultado:", number1,"/", number2,"=",number1/number2)       
          else: 
               print("No se puede dividir por 0")
     if Opcion == 5:
          number1=float(input("Ingrese primer numero:"))
          number2=float(input("ingreso segundo numero:"))
     if Opcion == 6:
          print("Gracias por utilizar la calculadora del curso de Python - CloudLamp eLearning")
