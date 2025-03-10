# Solicite um número inteiro ao usuário e exiba:
#O quociente e o resto da divisão por 7.

def calcular_divisao_por_7():
    try:
        # Solicita um número inteiro ao usuário
        numero = int(input("Digite um número inteiro: "))
        
        # Calcula o quociente e o resto da divisão por 7
        quociente = numero // 7  # Operação de divisão inteira
        resto = numero % 7  # Obtém o resto da divisão
        
        # Exibe os resultados
        print(f"O quociente da divisão por 7 é: {quociente}")
        print(f"O resto da divisão por 7 é: {resto}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")  # Trata erro caso o usuário insira valores inválidos

calcular_divisao_por_7()  # Chama a função para executar o programa

