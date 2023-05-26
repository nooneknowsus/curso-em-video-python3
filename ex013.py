salario = float(input("Digite o salário do funcionário: "))
aumento = salario + (salario * 15 / 100)

print(f"Salário bruto: R${salario}\nSalário com aumento de 15% R${aumento:.2f}")
