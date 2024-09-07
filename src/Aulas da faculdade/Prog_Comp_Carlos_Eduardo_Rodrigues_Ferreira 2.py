#atividade 1:
nome = "Carlos Eduardo Rodrigues Ferreira"

print (len(nome))


# atividade 2
for letra in nome:
    print(letra)

# atividade 3
name = input("Digite seu nome:\n")

cont = 0

for space in name:
     if space == ' ':
      cont = cont + 1


print(f"Meu nome tem {name} e tem {cont}\n")