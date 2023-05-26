from time import sleep

print("GERADOR DE PA\n")
termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão: "))

pa = termo
i = 1
inicio = 10
fim = 0

while inicio != 0:
    fim += inicio
    while i <= fim:
        print(f"{pa} -> ", end="")
        pa += razao
        i += 1
    print("Pausa")
    inicio = int(input("Quantos termos deseja ver a mais? "))

print(f"Programa fnalizado com {fim} termos mostrados!")
sleep(1)
print("Finalizando o programa.")