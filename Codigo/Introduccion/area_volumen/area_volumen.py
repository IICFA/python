# Programa que cálcula el área de una circunferencia y el volumen de una esfera dado un radio
import math

pi = math.pi

radio = float(input("Introduzca por favor el radio: "))

# área de la circunferencia
circulo = pi * radio**2

# volumén de una esfera
volumen = 4/3 * pi * radio ** 3

print("El área de la circunferencia radio", radio, "es:", circulo)
print("El volumen de la esfera de radio", radio, "es:", volumen)