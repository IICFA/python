# Programa que cálcula el área de una triángulo dado los lados
import math

L1 = float(input("Introduzca la longitud del lado1: "))
L2 = float(input("Introduzca la longitud del lado2: "))
L3 = float(input("Introduzca la longitud del lado3: "))

L = (L1 + L2 + L3)/2

area = math.sqrt(L * (L - L1) * (L - L2) * (L-L3))

print("EL área del triángulo es %.2f" % area)