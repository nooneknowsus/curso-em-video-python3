from math import hypot
catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))

'''hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print(f"A hipotenusa vai medir: {hipotenusa:.2f}")'''

hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f"A hipotenusa vai medir: {hipotenusa:.2f}")