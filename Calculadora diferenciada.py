print("Selecione a operação que deseja realizar:")
print("1. Soma (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
print("5. Potenciação (^)")
print("6. Raiz Quadrada (√)")

while True:
    operacao = input("Digite o número da operação (1/2/3/4/5/6): ")
    if operacao in ('1', '2', '3', '4', '5', '6'):
        break
    else:
        print("Escolha inválida. Por favor, selecione uma operação válida.")

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        if operacao in ('1', '2', '3', '4', '5'):
            num2 = float(input("Digite o segundo número: "))
        else:
            num2 = None
        if operacao == '1':
            print("Resultado:", num1 + num2)
        elif operacao == '2':
            print("Resultado:", num1 - num2)
        elif operacao == '3':
            print("Resultado:", num1 * num2)
        elif operacao == '4':
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Erro: Divisão por zero não é permitida.")
        elif operacao == '5':
            print("Resultado:", num1 ** num2)
        elif operacao == '6':
            if num1 < 0:
                print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
            else:
               print("Resultado: ", num1 ** 0.5)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

