# Programa que calcula el iva y la propina de la comida
IVA = 0.21
Propina = 0.18

monto_comida = float(input("¿Cuál es el monto de la comida? "))

# Cálculo de la propina, del IVA y del total
monto_IVA = IVA * monto_comida
monto_propina = Propina * monto_comida
total = monto_propina + monto_comida + monto_IVA

# Mostrar resultados:
print("La comida sale a %2.f $" % monto_comida)
print("EL IVA de %.2f sale a %.2f $" % (IVA, monto_IVA))
print("La propina a %.2f sale a %.2f $" % (Propina, monto_propina))
print("El monto total es de %.2f $" % total)
