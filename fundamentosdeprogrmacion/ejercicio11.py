def calcular_distancia(num1, num2):
    return abs(num1 - num2)

# Ejemplo de uso
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

distancia = calcular_distancia(num1, num2)

print(f"La distancia entre {num1} y {num2} es: {distancia}")

