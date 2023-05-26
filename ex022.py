nome = input("Digite seu nome completo: ").strip()
print("Analisando seu nome...")

print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem {len(nome.strip()) - nome.count(' ')} letras")

# split separa a string e pego o indice 0 que corresponde ao primeiro grupo de strings separadas
# no caso será o primeiro nome digitado.
print(f"Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras")
