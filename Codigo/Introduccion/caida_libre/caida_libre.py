# Programa que cálcula la velocidad final de la caida libre de un objeto
from math import sqrt
gravedad = 9.8  # m/s

altura = float(input("Introduzca los metros de altura: "))
vi = float(input("Introduzca los m/s de la velocidad inicial: "))

# Cálculo
vf = sqrt(vi**2 + 2 * gravedad * altura)

print("El objeto cae a una velocidad %.2f m/s" % vf)