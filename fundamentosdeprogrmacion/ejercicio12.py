import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Ejemplo de uso
x1 = float(input("Introduce la coordenada x1: "))
y1 = float(input("Introduce la coordenada y1: "))
x2 = float(input("Introduce la coordenada x2: "))
y2 = float(input("Introduce la coordenada y2: "))

distancia = calcular_distancia(x1, y1, x2, y2)

print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia:.2f}")
