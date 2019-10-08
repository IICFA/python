# Programa que transforma los kPa a libras por pulgadas**2, mm de mercurio y a atmosferas
kPa = float(input("Introduzca la cantidad de kPa a convertir: "))

# Fórmula  a libras por pulgadas**2
psi = kPa/6.895

# fórmula a mm de mercurio
mmhg = kPa * 7.50062

# fórmula a atmosfera
atm = kPa/101.325

print("la presión de %.6f es %.6f psi" % (kPa, psi))
print("la presión de %.6f es %.6f mmhg" % (kPa, mmhg))
print("la presión de %.6f es %.6f atm" % (kPa, atm))