# Solicite três números e exiba o maior e o menor entre eles, sem usar estruturas condicionais.

def encontrar_maior_menor():
    try:
        # Solicita três números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        
        # Usa funções built-in para encontrar o maior e o menor número
        maior = max(num1, num2, num3)  # Encontra o maior número
        menor = min(num1, num2, num3)  # Encontra o menor número
        
        # Exibe os resultados
        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")  # Trata erro caso o usuário insira valores inválidos

encontrar_maior_menor()  # Chama a função para executar o programa