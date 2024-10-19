def calcular_comisiones_y_sueldo_total(sueldo_base, ventas):
    comision = sum(venta * 0.10 for venta in ventas)
    sueldo_total = sueldo_base + comision
    return comision, sueldo_total

# Ejemplo de uso
sueldo_base = float(input("Introduce el sueldo base del vendedor: "))
ventas = []

for i in range(3):
    venta = float(input(f"Introduce el monto de la venta {i + 1}: "))
    ventas.append(venta)

comisiones, sueldo_total = calcular_comisiones_y_sueldo_total(sueldo_base, ventas)

print(f"Comisiones por ventas: {comisiones:.2f}")
print(f"Sueldo total del vendedor: {sueldo_total:.2f}")
