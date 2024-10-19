import math

def calcular_raiz_cuadrada(numero):
    return math.sqrt(numero)

def calcular_raiz_cubica(numero):
    return numero ** (1/3)

# Ejemplo de uso
numero = float(input("Introduce un número: "))

raiz_cuadrada = calcular_raiz_cuadrada(numero)
raiz_cubica = calcular_raiz_cubica(numero)

print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica:.2f}")

