# Solicite um número decimal e exiba:
# A raiz quadrada / A raiz cúbica / O quadrado do número

import math  # Importa a biblioteca 'math' para usar funções matemáticas como 'sqrt'

# Solicita ao usuário que digite um número decimal
numero = float(input("Digite um número decimal: "))

# Calcula a raiz quadrada utilizando a função 'sqrt' da biblioteca 'math'
raiz_quadrada = math.sqrt(numero)

# Calcula a raiz cúbica elevando o número a (1/3)
raiz_cubica = numero ** (1/3)

# Calcula o quadrado do número elevando o número a 2
quadrado = numero ** 2

# Exibe os resultados. A formatação '.2f' exibe os números com 2 casas decimais
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")
print(f"A raiz cúbica de {numero} é {raiz_cubica:.2f}")
print(f"O quadrado de {numero} é {quadrado:.2f}")

