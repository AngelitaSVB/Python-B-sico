# Solicite três números ao usuário e exiba a média ponderada, considerando os pesos 3, 2 e 5 para os três números, respectivamente.

def calcular_media_ponderada():
    try:
        # Solicita três números ao usuário e converte as entradas para float
        # O 'input()' solicita ao usuário que digite um valor, e 'float()' converte a entrada para um número decimal.
        num1 = float(input("Digite o primeiro número: "))  # Solicita o primeiro número
        num2 = float(input("Digite o segundo número: "))  # Solicita o segundo número
        num3 = float(input("Digite o terceiro número: "))  # Solicita o terceiro número
        
        # Define os pesos correspondentes a cada número
        # Os pesos são definidos como 3, 2 e 5 para os três números, respectivamente.
        peso1 = 3  # Peso do primeiro número
        peso2 = 2  # Peso do segundo número
        peso3 = 5  # Peso do terceiro número
        
        # Calcula a soma dos pesos
        # A soma dos pesos é feita simplesmente somando os valores dos pesos.
        soma_pesos = peso1 + peso2 + peso3  # Soma dos pesos: 3 + 2 + 5 = 10
        
        # Calcula a média ponderada
        # A fórmula da média ponderada é: 
        # (num1 * peso1 + num2 * peso2 + num3 * peso3) / soma dos pesos
        media_ponderada = (num1 * peso1 + num2 * peso2 + num3 * peso3) / soma_pesos
        
        # Exibe o resultado da média ponderada com duas casas decimais
        # A formatação '.2f' exibe o resultado com 2 casas decimais.
        print(f"A média ponderada é: {media_ponderada:.2f}")  # Exibe o valor com 2 casas decimais
    except ValueError:
        # Trata o erro se o usuário digitar algo que não seja um número
        # Caso o usuário insira texto ou outro valor inválido, o programa irá capturar o erro e exibir uma mensagem amigável.
        print("Por favor, digite apenas números válidos.")  # Mensagem de erro

# Chama a função para executar o cálculo
# Após definir a função, chamamos a função para executá-la e calcular a média ponderada.
calcular_media_ponderada()



