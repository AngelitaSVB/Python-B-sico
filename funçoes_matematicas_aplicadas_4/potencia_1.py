# Peça ao usuário para digitar dois números e exiba a potência do primeiro elevado ao segundo, utilizando pow()

# Solicita ao usuário que digite dois números
base = float(input("Digite o primeiro número (base): "))  # Solicita a base e converte para float
exponente = float(input("Digite o segundo número (exponente): "))  # Solicita o expoente e converte para float

# Calcula a potência usando a função pow()
potencia = pow(base, exponente)  # Calcula a potência de base^exponente

# Exibe o resultado
print(f"{base} elevado a {exponente} é igual a {potencia}")  # Exibe o resultado da operação
