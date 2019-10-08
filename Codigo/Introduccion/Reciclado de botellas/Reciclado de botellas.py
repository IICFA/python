# Calculador del monto por el reciclado de botellas
pequeño = 0.10 # Monto por botella de un litro o menor
grande = 0.25 # Monto por botella mayor de un litro

# Lee la cantidad de botellas pequeñas y grandes
botellas_pequeñas = int(input("¿Cuál es la cantidad de botellas igual o menores a un litro? "))
botellas_grandes = int(input("¿Cuál es la cantidad de botellas superiores a un litro? "))

# Cálcula el monto a pagar
total = pequeño * botellas_pequeñas + grande * botellas_grandes

# Muestra el resultado
print("El monto total es de $%.2f" % total)