def calcular_calificacion_final(calificaciones_parciales, examen_final, trabajo_final):
    promedio_parciales = sum(calificaciones_parciales) / len(calificaciones_parciales)
    calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
    return calificacion_final

# Ejemplo de uso
calificaciones_parciales = []
for i in range(3):
    calificacion = float(input(f"Introduce la calificación del parcial {i + 1}: "))
    calificaciones_parciales.append(calificacion)

examen_final = float(input("Introduce la calificación del examen final: "))
trabajo_final = float(input("Introduce la calificación del trabajo final: "))

calificacion_final = calcular_calificacion_final(calificaciones_parciales, examen_final, trabajo_final)

print(f"La calificación final en la materia de algoritmos es: {calificacion_final:.2f}")
