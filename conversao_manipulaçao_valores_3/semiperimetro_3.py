#Solicite o comprimento de três lados e exiba o semiperímetro do triângulo, calculando pela fórmula: s = (a + b + c) / 2
# Solicita ao usuário que digite os comprimentos dos três lados
a = float(input("Digite o comprimento do primeiro lado: "))  # Converte a entrada para float para permitir valores decimais
b = float(input("Digite o comprimento do segundo lado: "))  # Converte a entrada para float
c = float(input("Digite o comprimento do terceiro lado: "))  # Converte a entrada para float

# Calcula o semiperímetro usando a fórmula s = (a + b + c) / 2
semiperimetro = (a + b + c) / 2  # Soma os três lados e divide por 2 para calcular o semiperímetro

# Exibe o semiperímetro
print(f"O semiperímetro do triângulo é: {semiperimetro}")  # Exibe o semiperímetro calculado


