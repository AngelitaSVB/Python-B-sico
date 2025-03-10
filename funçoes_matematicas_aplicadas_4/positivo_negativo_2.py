# Peça ao usuário um número positivo ou negativo e exiba seu valor absoluto.

# Explicação:
# input(...): Solicita ao usuário que insira um número (pode ser positivo ou negativo).
# float(...): Converte a entrada do usuário para um número decimal (tipo float) para permitir valores decimais.
# abs(...): A função abs() retorna o valor absoluto do número, ou seja, o número sem o sinal negativo, se houver.
# print(...): Exibe o valor absoluto do número inserido.

# Solicita ao usuário que digite um número
numero = float(input("Digite um número (positivo ou negativo): "))  # Solicita um número e converte para float

# Calcula o valor absoluto do número usando a função abs()
valor_absoluto = abs(numero)  # A função abs() retorna o valor absoluto do número

# Exibe o valor absoluto
print(f"O valor absoluto de {numero} é {valor_absoluto}")  # Exibe o resultado

