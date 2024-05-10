# Solicita ao usuário que insira o primeiro dado e verifica se é uma string
while True:
    dado1 = input("Digite o seu primeiro dado: ")
    if dado1.isalpha():
        break
    else:
        print("Por favor, insira apenas letras.")

# Solicita ao usuário que insira o segundo dado e verifica se é uma string
while True:
    dado2 = input("Digite o seu segundo dado: ")
    if dado2.isalpha():
        break
    else:
        print("Por favor, insira apenas letras.")

# Concatena os dados apenas se ambos forem strings
dados_concatenado = dado1 + " " + dado2

print(f"Seus dados concatenados são: {dados_concatenado}")
