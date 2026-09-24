nome = input("Digite seu nome: ")
valor_compra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o valor do desconto (em %): "))

print(f"Olá {nome}, sua compra de R${valor_compra:.2f} foi confirmada!")

valor_final = valor_compra - (valor_compra * (desconto / 100))

print(f"Foi aplicado um desconto de {desconto:.2f}%")  
print(f"O valor total ficou em R${valor_final:.2f}")