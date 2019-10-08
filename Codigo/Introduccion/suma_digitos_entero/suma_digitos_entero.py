# Programa que lee un entero de 4 digitos y muestra la suma de los digitos.

# Contador de digitos
def digitos_cantidad(n):
    cantidad = 1

    while n > 9:
        n = n // 10
        cantidad = cantidad + 1

    return cantidad

def suma_digitos(n):
    total = 0

    while n > 9:
        digito = n % 10
        n = n // 10
        total = total + digito

    return total + digito

numero = int(input("Introduzca el entero de 4 dígitos: "))

# Comprobar si el entero tiene 4 dígitos
if digitos_cantidad(numero) == 4:
    print(" ")
    print("La suma de los dígitos es", suma_digitos(numero))
else:
    print("Error: el número es distinto a 4 dígitos")
    print(digitos_cantidad(numero))


