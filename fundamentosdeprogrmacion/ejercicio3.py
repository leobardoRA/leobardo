import math

def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa

# Ejemplo de uso
cateto_a = float(input("Introduce la longitud del primer cateto: "))
cateto_b = float(input("Introduce la longitud del segundo cateto: "))
hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

print(f"La hipotenusa del triángulo rectángulo es: {hipotenusa:.2f}")
