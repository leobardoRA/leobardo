def convertir_minutos_a_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

# Ejemplo de uso
minutos = int(input("Introduce la cantidad de minutos: "))

horas, minutos_restantes = convertir_minutos_a_horas(minutos)

print(f"{minutos} minutos son equivalentes a {horas} horas y {minutos_restantes} minutos.")

