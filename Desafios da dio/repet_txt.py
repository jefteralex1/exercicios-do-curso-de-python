while True:
    string = input("Digite o seu primeiro dado: ")
    if string.isalpha():
        break
    else:
        print("Por favor, insira apenas letras.")

while True:
    vezes = input("Digite o número de vezes: ")
    if vezes.isdigit():
        vezes = int(vezes)  # Convertendo a entrada para um número inteiro
        break
    else:
        print("Por favor, insira apenas números.")

print(string * vezes)
