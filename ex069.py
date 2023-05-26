import string
from time import sleep

maioridade = 0
homens = 0
mulheres = 0
mulheres_menor = 0

while True:
    idade = int(input("Digite a sua idade: "))
    sexo = ' '
    while sexo not in "MF":

        sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]

    if idade >= 18:
        maioridade += 1
    if sexo == "F" and idade < 20:
        mulheres_menor += 1
    elif sexo == "M":
        homens += 1


    opcao = ' '
    while opcao not in "SN":
        opcao = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]

    if opcao == "N":
            break

    else:
        print("\nPróximo cadastro\n")

print(20 * "--")
print(f'''Total de pessoas com mais de 18 anos: {maioridade}
Ao todo temos {homens} homens cadastrados
E temos {mulheres_menor} mulheres com menos de 20 anos''')
print(20 * "--")