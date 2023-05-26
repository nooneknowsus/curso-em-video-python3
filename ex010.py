real = float(input("Quanto dinheiro você tem na carteira? "))

dolar = real / 5.25
euro = real / 5.63
iene = real * 25.38

print(f"Com R${real}, você pode comprar U${dolar:.2f}")
print(f"€{euro:.2f} e ¥{iene}")
