# Programa que cálcula la cantidad de días, horas, minutos dado unos segundos
s_por_dia = 86400
s_por_h = 3600
s_por_min = 60

segundos = int(input("Introduzca la cantidad de segundos: "))

dias = segundos / s_por_dia
segundos = segundos % s_por_dia

horas = segundos / s_por_h
segundos = segundos % s_por_h

minutos = segundos / s_por_min
segundos = segundos % s_por_min

print("La duración equivalente es %d:%02d:%02d:%02d " %(dias, horas, minutos, segundos))