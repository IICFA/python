# Cálcula el peso en gramos de los productos
artilugios = 112 # gramos
componentes = 75 # gramos

# Input
cant_artilugios = int(input("Indique por favor la cantidad de artilugios "))
cant_componentes = int(input("Indique por favor la cantidad de componentes "))

#Peso total
Total_peso = cant_artilugios * artilugios + componentes * cant_componentes

# Mostrar resultados
print(" el peso total en gramos es", Total_peso)