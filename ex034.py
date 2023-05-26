salario = float(input("Digite seu salário: R$"))
if salario > 1250:
    salario = salario + (salario * 10 / 100)
    print(f"Com reajuste de 10% seu salário passa a ser R${salario}")
else:
    salario = salario + (salario * 15 / 100)
    print(f"Com reajuste de 15% seu salário passa a ser R${salario}")

