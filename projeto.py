mes_escrito = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",]

somaTemperaturas = 0
qtdMesesEscandantes = 0
mesMenosQuente = 0
mesMaisQuente = 12
temperaturaMaisQuente = -61
temperaturaMenosQuente = 51

for mes in range (1,13):

    while True:
        try:
            temperatura = float(input(f"Informe a temperatura máxima de {mes_escrito[mes-1]} (em °C): "))
            if temperatura < -60 or temperatura > 50 :
                print ("Temperatura inválida, digite entre [-60;50].")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    

    somaTemperaturas += temperatura

    if temperatura > temperaturaMaisQuente:
        temperaturaMaisQuente = temperatura
        mesMaisQuente = mes


    if temperatura < temperaturaMenosQuente:
        temperaturaMenosQuente = temperatura
        mesMenosQuente = mes

    if temperatura > 33:
        qtdMesesEscandantes += 1

mediaTemperaturas = somaTemperaturas / 12
print (f"Media de temperaturas máximas: {mediaTemperaturas:.1f}°C")

print(f"Quantidade de meses escaldantes: {qtdMesesEscandantes} { 'mes' if qtdMesesEscandantes == 1 else 'meses' }")


print(f"Mes mais escaldantes do ano: {mes_escrito[mesMaisQuente-1]}")
print(f"Temperatura: {temperaturaMaisQuente}°C")

print(f"Mes menos quente do ano: {mes_escrito[mesMenosQuente-1]}")
print(f"Temperatura: {temperaturaMenosQuente}°C")