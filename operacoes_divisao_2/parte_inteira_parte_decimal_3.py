#Solicite um número decimal e exiba a parte inteira e a parte decimal separadamente.

# Solicita ao usuário que digite um número decimal
numero_decimal = float(input("Digite um número decimal: "))

# Obtém a parte inteira do número usando a função int()
parte_inteira = int(numero_decimal)

# Obtém a parte decimal subtraindo a parte inteira do número original
parte_decimal = numero_decimal - parte_inteira

# Exibe a parte inteira e a parte decimal separadamente
print(f"A parte inteira é: {parte_inteira}")
print(f"A parte decimal é: {parte_decimal}")
