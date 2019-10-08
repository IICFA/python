# Programa que cálcula el área de un polígono regular
import math

L = float(input("Indique la longitud de los lados: "))
n = int(input("Indique el número de lados: "))

area = (n * L ** 2) / (4 * math.tan(math.radians(math.pi / n)))

print("El área del polígono es %.2f " % area)