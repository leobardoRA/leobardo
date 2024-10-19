def invertir_numero(numero):
    # Convertir el número a cadena para poder invertirlo
    return str(numero)[::-1]

# Ejemplo de uso
numero = int(input("Introduce un número de dos cifras: "))

# Verificar que el número tenga dos cifras
if 10 <= numero <= 99:
    numero_invertido = invertir_numero(numero)
    print(f"El número invertido de {numero} es: {numero_invertido}")
else:
    print("Por favor, introduce un número de dos cifras.")
