# Programa que cálcula el monto generado en una cuenta de interés compuesto
interes_anual = 0.04

#Input años y monto inicial
años = int(input("Cantidad de años de la cuenta "))
monto_inicial = float(input("Monto inicial de la cuenta "))

#Formula interés compuesto
monto_final = monto_inicial * (1 + interes_anual)**años

# Mostrar resultados
print("El monto total generado es %.2f $" % monto_final)