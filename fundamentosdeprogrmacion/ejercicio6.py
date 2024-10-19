def calcular_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

# Ejemplo de uso
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

media = calcular_media(num1, num2, num3)

print(f"La media de los tres números es: {media:.2f}")

