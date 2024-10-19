def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    # Verificar que no se divida entre cero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "No se puede dividir entre cero"

    return suma, resta, multiplicacion, division

# Ejemplo de uso
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


