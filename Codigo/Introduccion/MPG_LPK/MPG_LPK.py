# Programa que convierte las millas/galon a litros/100km
convertidor = 235.21 # 1 MPG = 235,21 litros/100 km

mpg = float(input(" Introduzca por favor la cantidad de millas por galón: "))
L100km = mpg * convertidor

print("EL total de litros/100km es:", L100km)