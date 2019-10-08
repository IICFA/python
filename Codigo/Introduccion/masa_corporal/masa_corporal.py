# Programa que cálcula la masa corporal dado la altura y el peso
altura = float(input("Introduzca la altura en metros: "))
peso = float(input("Introduzca el peso en kg: "))

# Fórmula del indice de masa corporal
IMC = peso/altura**2

print("EL indice de masa corporal es: %.2f" % IMC)