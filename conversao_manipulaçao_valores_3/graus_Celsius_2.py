# Peça ao usuário um valor em graus Celsius e converta para Fahrenheit e Kelvin.

# Solicita ao usuário que digite um valor em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte Celsius para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Converte Celsius para Kelvin
kelvin = celsius + 273.15

# Exibe os resultados
print(f"{celsius} graus Celsius correspondem a {fahrenheit} graus Fahrenheit.")
print(f"{celsius} graus Celsius correspondem a {kelvin} Kelvin.")