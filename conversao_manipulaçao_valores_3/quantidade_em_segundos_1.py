#Solicite uma quantidade em segundos ao usuário e exiba o valor correspondente em horas, minutos e segundos.

# Solicita ao usuário que digite a quantidade de segundos
segundos = int(input("Digite a quantidade de segundos: "))  # Converte a entrada do usuário em um número inteiro

# Calcula o número de horas
horas = segundos // 3600  # A divisão inteira (//) converte os segundos para horas, dividindo por 3600 (segundos em uma hora)

# Calcula os minutos restantes após a conversão para horas
minutos = (segundos % 3600) // 60  # O operador % calcula o resto da divisão por 3600 (segundos que sobram após converter para horas), 
                                  # e em seguida, a divisão inteira por 60 converte esses segundos restantes em minutos.

# Calcula os segundos restantes após a conversão para minutos
segundos_restantes = segundos % 60  # O operador % calcula os segundos que sobram depois de dividir os minutos (resto da divisão por 60).

# Exibe o resultado em horas, minutos e segundos
print(f"{segundos} segundos correspondem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")  # Exibe o resultado final formatado
