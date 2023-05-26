valorCasa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$"))
anosPagamento = int(input("Digite em quantos anos você vai pagar: "))

parcelas = valorCasa / (anosPagamento * 12)
limite = (salario * 30 / 100)

print(f"Para pagar uma casa de R${valorCasa} em {anosPagamento} anos\nA prestação será de R${parcelas:.2f}\n")

if parcelas >= limite:
    print("Empréstimo negado")
else:
    print("Empréstimo aceito")