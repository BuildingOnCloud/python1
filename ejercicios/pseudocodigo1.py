float impuesto = 0,15
integer nro_articulos_comprados = 7
float subtotal = 0.0
float subtotal_impuesto = 0.0
float total_general = 0.0

for i in range(1..nro_articulos_comprados):
    input(precio_articulo)
    subtotal = subtotal + precio_articulo

subtotal_impuesto = subtotal * impuesto
total_general = subtotal + subtotal_impuesto

print(subtotal)
print(subtotal_impuesto)
print(total_general)