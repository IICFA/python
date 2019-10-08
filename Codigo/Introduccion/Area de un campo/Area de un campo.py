#Programa que cálcula el área de un campo en acres
sqft_per_acre = 43560

#leer input del usuario
largo = float(input("¿Cuál es el largo del campo en pies? "))
ancho = float(input("Cuál es el ancho en pies del campo? "))

#Área en acres
acres = largo * ancho/sqft_per_acre

#Mostrar resultado
print("El área del campo es", acres,"acres.")