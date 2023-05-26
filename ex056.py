acumulador = 0
maior = 0
menor = 0
nome_maior = ''
cont_idade = 0
cont_homens = 0
cont_mulheres = 0
for c in range(1, 5):
    print(f"{5*'-'} {c}º Pessoa {5*'-'}")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()

    if sexo == "M":
        cont_homens += 1
        if idade >= maior:
            maior = idade
            nome_maior = nome

    if sexo == "F":
        cont_mulheres += 1
        if idade < 20:
            cont_idade += 1

    acumulador += idade

media = acumulador / 4
print(f"A média de idade do grupo é {media} ano(s).")

if cont_homens == 0:
    print("Não foi encontrado nenhum registro do sexo masculino")
else:
    print(f"O homem mais velho tem {maior} anos e se chama {nome_maior}.")

if cont_mulheres == 0:
    print("Não foi encontrado nenhum registro do sexo feminino.")
else:
    print(f"Ao todo são {cont_idade} mulher(es) com menos de 20 anos.")