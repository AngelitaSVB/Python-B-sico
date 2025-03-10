#Solicite ao usuário dois números inteiros positivos e calcule o Mínimo Múltiplo Comum (MMC) entre eles (dica: use a relação entre o MMC e o MDC).

# Função para calcular o Máximo Divisor Comum (MDC) usando o algoritmo de Euclides
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicita ao usuário dois números inteiros positivos
a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))

# Calcula o MDC entre os dois números
mdc_ab = mdc(a, b)

# Calcula o MMC usando a relação entre MMC e MDC
mmc_ab = (a * b) // mdc_ab

# Exibe o MMC calculado
print(f"O Mínimo Múltiplo Comum (MMC) entre {a} e {b} é: {mmc_ab}")
