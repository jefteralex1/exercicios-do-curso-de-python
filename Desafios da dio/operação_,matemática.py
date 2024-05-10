# Solicita ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada ao usuário
operacao = input("Escolha a operação desejada (+ para adição, - para subtração, * para multiplicação, / para divisão): ")

# Executa a operação escolhida pelo usuário e exibe o resultado
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:  # Verifica se o segundo número não é zero para evitar divisão por zero
        resultado = num1 / num2
    else:
        print("Não é possível dividir por zero.")
        resultado = None
else:
    print("Operação inválida.")
    resultado = None

# Exibe o resultado da operação, se houver
if resultado is not None:
    print(f"O resultado da operação é: {resultado}")
