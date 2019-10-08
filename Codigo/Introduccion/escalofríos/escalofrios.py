# Progrma que cálcula el factor de enfriamiento del viento
temperatura = float(input("Introduzca la temperatura del aire en ºC: "))
v = float(input("Introduzca la velocidad del viento en km/h: "))

# fórmula
FEV = 13.2 + 0.6215 * temperatura - 11.37 * v**0.16 + 0.3965 * temperatura * v**0.16

FEV = round(FEV)

print("El factor de enfriamiento del viento es: ", FEV)
