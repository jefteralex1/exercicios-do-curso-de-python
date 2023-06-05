#crie um programa que leia um número e mostre seu dobro, triplo e sua raiz quadrada.
num = int(input("Digite um numero: "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f"O dobro de {num} vale {dobro}")
print(f"O triplo de {num} vale {triplo}")
print(f"A raiz quadrada de {num} vale {raiz}")