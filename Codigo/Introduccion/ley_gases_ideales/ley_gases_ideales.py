# Programa que cálcula la cantidad de moles de una gas usando la ley de gases ideales
R = 8.314  # j/(mol * K)

P = float(input("Introduzca los Pa: "))
T = float(input("Introduzca los ºC: "))
V = float(input("Introduzca el volumen en litros: "))

# Fórmula
n = P * V/(R * (T + 273.15))

print(" la cantidad de moles del gas es %.0f" % n)