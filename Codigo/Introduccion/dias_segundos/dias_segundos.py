# Programa que cálcula los segundos según el tiempo dado
s_por_dia = 86400
s_por_h = 3600
s_por_min = 60

dias = int(input("Introduzca el número de días: "))
horas = int(input("Inroduzca la cantidad de horas: "))
minutos = int(input("Introduzca la cantidad de minutos: "))

segundos = (s_por_dia * dias) + s_por_h * horas + s_por_min * minutos

print("Los segundos totales son:", segundos)