"""

programa que calcule el area y el perimetro de un rectagulo a partir de su base y su altura 
Entradas:
base:integer
altura:integer
salida:
perimetro:integer
area:integer
analisis:
print("se requiere calcular con las formulas para area y perimetro")

"""

#input siempre regresa un string
#para tatarlo como otro dato se debe convetir
print("programa que calcula area y perimetrode un rentagulo") 
base =input("Esribe la base del rectagulo:")
base = int(base)
altura =input("Escribe la altura del rectagulo:")
altura = int(altura)
area = base + base + altura + altura
perimetro = (base + altura)* 2
print("El area de rectagulo es " +str(area))
print("El area del rectagulo es ", perimetro)
print(area)
print(perimetro)