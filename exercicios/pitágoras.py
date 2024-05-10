'''O Teorema de Pitágoras é uma das mais famosas proposições matemáticas atribuídas a Pitágoras, um matemático grego antigo. 
    Ele estabelece uma relação fundamental entre os comprimentos dos lados de um triângulo retângulo, ou seja, um triângulo que possui um ângulo reto (90 graus).

De acordo com o teorema:
    Em um triângulo retângulo, o quadrado da medida da hipotenusa (o lado oposto ao ângulo reto) é igual à soma dos quadrados das medidas dos outros dois lados.

    Se a, b e c são os comprimentos dos lados de um triângulo retângulo, com c sendo a medida da hipotenusa, então:
        c² = a² + b²
'''

def calcular_hipotenusa(a, b):
    hipotenusa = (a**2 + b**2)**0.5
    return hipotenusa

def main():
    print("Digite o comprimento dos catetos do triângulo retângulo:")
    a = float(input("Comprimento do primeiro cateto (a): "))
    b = float(input("Comprimento do segundo cateto (b): "))
    
    hipotenusa = calcular_hipotenusa(a, b)
    
    print("O comprimento da hipotenusa é:", hipotenusa)

if __name__ == "__main__":
    main()
