# Programa que calcula la longitud y la latitud entre dos puntos
import math

grados_lat1 = math.radians(float(input("introduzca por favor los grados de la latitud: ")))
grados_long1 =  math.radians(float(input("introduzca los grados de la longitud: ")))
grados_lat2 =  math.radians(float(input("Introduzca los grados de la latitud2: ")))
grados_long2 =  math.radians(float(input("Introduzca los grados de la longitud2: ")))

# Fórmula de conversión = 6371.01 * arcos(sin(t1) * sin(t2) + cos(t1) * cos(t2) x ( cos(g1-g2))
distancia = 6371.01 * math.acos(math.sin(grados_lat1) * math.sin(grados_lat2) + math.cos(grados_lat1) *
                                math.cos(grados_lat2) * math.cos(grados_long1-grados_long2))

print("La distancia entre los dos puntos es:", distancia)