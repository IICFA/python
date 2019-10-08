# Programa que cálcula el monto necesario de energía para elevar la temperatura del agua a cierto ºC
capacidad_calo_agua = 4.186  # j/ºC
costo_electricidad = 8.9  # céntimos
densidad_agua = 1  # 1 g/ml
joules_kWh = 2.77778e-7

delta_temperatura = float(input("Introduzca la temperatura en ºC deseada a cambiar: "))
masa = float(input("Introduzca los gramos de agua a calentar: "))

# Cálculo
q = masa * delta_temperatura * capacidad_calo_agua
kWh = q * joules_kWh
costo = kWh * costo_electricidad

print("Se necesitan %.d Joules" %q)
print("lo que equivale a %.6f kWh" % kWh)
print("Con un costo total %.2f céntimos" % costo)