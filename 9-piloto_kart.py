tamanho_da_pista = float(input("Digite o tamanho da pista em metros: "))
quantidade_de_voltas = int(input("Digite a quantidade de voltas: "))
tempo_por_volta = float(input("Digite o tempo por volta em segundos: "))

distancia_total = tamanho_da_pista * quantidade_de_voltas
previsao_tempo_total = tempo_por_volta * quantidade_de_voltas

print("Análise Preditiva de Corrida")
print("--")
print(f"Distância total a ser percorrida: {distancia_total / 1000:.2f} km")
print(f"Previsão de conclusão: {previsao_tempo_total / 60:.2f} minutos")