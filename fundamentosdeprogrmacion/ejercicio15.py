# Solicitar al usuario que ingrese los valores de A y B
A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

# Mostrar los valores originales
print(f"Valores originales: A = {A}, B = {B}")

# Intercambiar los valores de A y B
A, B = B, A

# Mostrar los valores intercambiados
print(f"Valores intercambiados: A = {A}, B = {B}")
