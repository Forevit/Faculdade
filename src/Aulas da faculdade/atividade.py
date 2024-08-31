nome_usuario = input ("Digite o seu nome: ")
sobrenome = input ("Digite o seu sobrenome: ")
endereco = input ("Me diga o seu endereço: ")

aprensentacao = (f"Meu nome é {nome_usuario} {sobrenome} e eu moro na {endereco}")

print(aprensentacao)

nome_invertido = ''.join(reversed(nome_usuario))
print(nome_invertido)