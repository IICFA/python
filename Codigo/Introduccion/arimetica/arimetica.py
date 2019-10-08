# Programa que realiza operaciones básicas de matemáticas dado 2 números
from math import log10
a = int(input("introduce el primer número entero "))
b = int(input("Introduce el segundo número entero "))

sum = a + b
resta = a - b
producto = a * b
cociente = a / b
resto = a % b
log_10 = log10(a)
potencia = a ** b

print(a, " +", b, "=", sum)
print(a, "-", b, "=", resta )
print(a, "*",b, "=", producto)
print(a, "/", b, "=", cociente)
print(a, "%", b, "=", resto)
print(" el log10 de a es ", log_10)
print(a, "^", b, "=", potencia)
