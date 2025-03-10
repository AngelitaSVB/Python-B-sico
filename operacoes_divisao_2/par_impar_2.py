#Peça ao usuário um número e exiba se ele é par ou ímpar (dica: use % 2 e a diferença entre 0 e 1 no resultado).

# Solicita ao usuário que digite um número e converte a entrada para inteiro
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 2 sem deixar resto (módulo 2 igual a 0)
if numero % 2 == 0:
    # Se o número for divisível por 2, ele é par
    print(f"O número {numero} é par.")
else:
    # Caso contrário, o número é ímpar
    print(f"O número {numero} é ímpar.")