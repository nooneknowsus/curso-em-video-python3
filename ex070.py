from time import sleep

print(20 * "--")
print(f"LOJA SUPER BARATÃO")
print(20 * "--")

totvalorcompra = produtos_mil = valor_barato = produtos = 0
nome_barato = ""

while True:
    nome = str(input("Nome do produto: ")).split()
    produtos += 1
    valor = int(input("Preço: R$"))
    totvalorcompra += valor

    if produtos == 1:
        valor_barato = valor


    if valor <= valor_barato:
        valor_barato = valor
        nome_barato = nome

    if valor > 1000:
        produtos_mil += 1

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]

    if opcao == "N":
        break
    else:
        print("\nPróximo produto\n")

print("Finalizando o programa\n")
sleep(2)
print(20 * "--")
print(f"O total da compra foi de R${totvalorcompra}")
print(f"Temos {produtos_mil} custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_barato} que custa R${valor_barato}")
print(20 * "--")
