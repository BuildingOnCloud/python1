print("Factura de Compra")
print("------------------")
print("Nombre del producto:")
producto = input()
print("cantidad de", producto)
p_cantidad = int(input())
print("Valor unitario de", producto)
p_unitario = float(input())

p_st = p_cantidad * p_unitario

subTotal = p_st
IVA = subTotal *0.15
Total = subTotal + IVA

print ("--------------------")

print ("    Sub-Total:" ,p_st)
print ("          IVA:" ,IVA)
print ("Total a pagar:" ,Total)
input()