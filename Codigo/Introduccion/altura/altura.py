# Programa que convierte los pies y pulgadas a cm
pies_pulgadas = 12  # 12 pulgadas es un pie
pulgadas_cm = 2.54  # 1 pulgada es 2,54 cm

pies = int(input("Introduzca el total de pies de altura: "))
pulgadas = float(input("Introduzca el total de pulgadas de altura: "))

# Conversor
altura = (pies * pies_pulgadas + pulgadas) * pulgadas_cm

print("El total de cm de altura es", altura)
