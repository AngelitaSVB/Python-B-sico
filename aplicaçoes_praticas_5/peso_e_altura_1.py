#Peça ao usuário para informar seu peso e altura e calcule o Índice de Massa Corporal (IMC): peso / altura ** 2.

# Solicita ao usuário o peso e a altura
peso = float(input("Digite o seu peso em kg: "))  # Converte a entrada para float para permitir valores decimais
altura = float(input("Digite a sua altura em metros: "))  # Converte a entrada para float

# Calcula o IMC usando a fórmula IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)

# Exibe o IMC calculado
print(f"O seu Índice de Massa Corporal (IMC) é: {imc:.2f}")  # Exibe o IMC com 2 casas decimais
