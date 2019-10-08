# Programa que ordena de manera ascendente 3 números introducidos
n1 = int(input("Introduzca el primer número: "))
n2 = int(input("Introduzca el segundo número: "))
n3 = int(input("Introduzca el tercer número: "))

mn = min(n1, n2, n3)
mx = max(n1, n2, n3)
md = n1 + n2 + n3 - mx -mn

print("Los numeros es orden son:", mn, md, mx)
