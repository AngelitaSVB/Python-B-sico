#Solicite a distância percorrida (em km) e o tempo gasto (em horas) para calcular a velocidade média de um veículo.

# Solicita ao usuário a distância percorrida em quilômetros e o tempo gasto em horas
distancia = float(input("Digite a distância percorrida em km: "))  # Converte a entrada para float
tempo = float(input("Digite o tempo gasto em horas: "))  # Converte a entrada para float

# Calcula a velocidade média usando a fórmula: velocidade = distancia / tempo
velocidade_media = distancia / tempo

# Exibe a velocidade média calculada
print(f"A velocidade média do veículo é: {velocidade_media:.2f} km/h")  # Exibe a velocidade média com 2 casas decimais
