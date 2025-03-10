# Peça ao usuário para informar um número decimal e exiba:
# O valor arredondado para cima
# O valor arredondado para baixo
# O valor truncado (sem casas decimais)

import math  # Importa a biblioteca 'math', que contém funções como ceil, floor e trunc

def processar_numero():
    try:
        # Solicita um número decimal ao usuário
        # O 'input()' captura a entrada do usuário como uma string e 'float()' converte para número decimal.
        numero = float(input("Digite um número decimal: "))  
        
        # Arredonda o número para cima utilizando a função 'ceil' da biblioteca 'math'
        arredondado_cima = math.ceil(numero)  # O 'ceil' arredonda para o próximo número inteiro maior ou igual
        
        # Arredonda o número para baixo utilizando a função 'floor' da biblioteca 'math'
        arredondado_baixo = math.floor(numero)  # O 'floor' arredonda para o número inteiro menor ou igual
        
        # Trunca o número, removendo as casas decimais, utilizando a função 'trunc' da biblioteca 'math'
        truncado = math.trunc(numero)  # O 'trunc' remove as casas decimais, sem arredondar
        
        # Exibe os resultados
        print(f"Arredondado para cima: {arredondado_cima}")  # Exibe o número arredondado para cima
        print(f"Arredondado para baixo: {arredondado_baixo}")  # Exibe o número arredondado para baixo
        print(f"Truncado (sem casas decimais): {truncado}")  # Exibe o número truncado
        
    except ValueError:
        # Trata o erro caso o usuário digite algo que não seja um número válido
        print("Por favor, digite um número decimal válido.")  # Mensagem de erro

# Chama a função para executar o programa
processar_numero()  # A função é chamada para rodar o código

