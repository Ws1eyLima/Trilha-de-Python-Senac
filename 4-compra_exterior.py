valor_a_converter = float(input("Digite o valor em real que deseja converter para doláres: "))

COTACAO_DOLAR = 5.42

print(f"Valor em real: R$ {valor_a_converter:.2f}")
print(f"Valor em dólares: US$ {valor_a_converter / COTACAO_DOLAR:.2f}") 
