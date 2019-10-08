# Programa para el cálculo de linea de sistema de un equipo multidianóstico
import sys

ro20_cobre = 0.018
ro20_aluminio = 0.029
alfa_cobre = 0.00392
alfa_aluminio = 0.00403
error = 0

# Input de los datos para determinar los datos
RTotal = float(input(
    "El valor de la resistencia en ohmios es menor igual a "))  # siendo esta medida entre dos fases: desde el punto de alimentación al armario del generador.'''
R0 = float(input("El valor de la resistencia interna  en ohmios del transformador de alimentacion es igual a "))
R2 = float(input("Resistencia del contacto de aparellaje, contactor y protecciones, aproximadamente en ohmios es "))
material_R3 = input(" Material de la línea de acometida entre el cuadro de protección y el armario generador ")
temperatura_R3 = float(input(
    "Temperatura en centigrados de trabajo de la línea de acometida entre el cuadro de protección y el armario generador "))
seccion_R3 = float(input("Tamaño de la seccion en milimetros cuadrados de la línea de acometida entre el cuadro de protección y el armario generador "))
longitud_R3 = float(input("Longitud (ida) en metros de la línea de acometida entre el cuadro de protección y el armario generador "))
material_R1 = input("Material de la línea de acometida entre el transformador y el cuadro de protección medida entre dos fases ")
temperatura_R1 = float(input("Temperatura en centigrados de la línea de acometida entre el transformador y el cuadro de protección medida entre dos fases "))
longitud_R1 = float(input("Longitud (ida) en metros de la línea de acometida entre el transformador y el cuadro de protección medida entre dos fases "))


# Definición de la variable ro dependiente del tipo de material y de la temperatura
def ro(material, temperatura):
    if material == "cobre" or material == "Cobre":
        ro_temperatura = ro20_cobre * (1 + alfa_cobre * (temperatura - 20))
    elif material == "aluminio" or material == "Aluminio":
        ro_temperatura = ro20_aluminio * (1 + alfa_aluminio * (temperatura - 20))
    else:
        print(" ")
        print("EL material indicado no se reconoce en la base de datos")
        sys.exit(1)
    return (ro_temperatura)


# Determinación de R3
R3 = ro(material_R3, temperatura_R3) * 2 * longitud_R3 / seccion_R3  # Se multiplica por 2 por ser ida y vuelta

# Cálculo de R1
R1 = RTotal - R0 - R2 - R3
if R1 < 0:
    print(" ")
    print("R1 no puede ser negativo")
    sys.exit(1)

# Muestra el valor de R3 y R1
print(" ")
print("El valor de R3 es", R3, "ohmios")
print("El valor de R1 es igual o menor a", R1, "ohmios")

# Cálculo de la sección de la línea de acometida entre el transformador y el cuadro de protección medida entre dos fases
S1 = ro(material_R1, temperatura_R1) * 2 * longitud_R1 / R1

# Mostrar el resultado
print("El valor de la sección de la línea de acometida entre el transformador y el cuadro de protección es de ", S1, "milimetros cuadrados")