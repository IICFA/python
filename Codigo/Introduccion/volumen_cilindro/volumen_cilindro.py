# Programa que cálcula el volumen de un cilindro
import math

radio = float(input("Introduzca el radio deseado: "))
altura = float(input("Introduzca la altura: "))

volumen = round(altura * math.pi * radio ** 2, 1)

print("el volumen del cilindro es:", volumen)