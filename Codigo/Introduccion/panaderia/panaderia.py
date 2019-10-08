# Programa que muestra el precio, descuento y total de una cantidad de pan comprados
precio_pan = 3.49
descuento = 0.6

cantidad_pan = int(input("Introduzca la cantidad de pan a comprar: "))

precio_regular = precio_pan * cantidad_pan
precio_descuento = descuento * precio_regular
total = precio_regular - precio_descuento

print("El precio regular es: %5.2f" % precio_regular)
print("El descuento es de:   %5.2f" % precio_descuento)
print("El precio total es:   %5.2f" % total)