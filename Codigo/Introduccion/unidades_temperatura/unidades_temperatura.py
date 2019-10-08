# Programa que transforma los ºC a Fahrenheit y Kelvin
grados_C = float(input("Introduzca la cantidad de ºC a convertir: "))

# Fórmula Fahrenheit
F = (grados_C + 9/5) + 32

# Fórmula Kelvin
K = grados_C + 273.15

print("Los %.2f ºC equivalen a %.2f ºF o a %.2f ºK" % (grados_C, F, K))
