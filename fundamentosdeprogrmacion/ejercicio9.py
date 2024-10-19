def calcular_total_con_descuento(total_compra):
    descuento = total_compra * 0.15
    total_a_pagar = total_compra - descuento
    return descuento, total_a_pagar

# Ejemplo de uso
total_compra = float(input("Introduce el total de la compra: "))

descuento, total_a_pagar = calcular_total_con_descuento(total_compra)

print(f"Descuento aplicado: {descuento:.2f}")
print(f"Total a pagar después del descuento: {total_a_pagar:.2f}")

