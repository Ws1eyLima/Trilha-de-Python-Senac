peso_comprado = int(input("Selecione o peso de sorvetes comprados em g: "))

PRECO_100G = 3.50

if peso_comprado <= 0:
    print("Peso Inválido")
elif peso_comprado < 1000:
    valor_total = (peso_comprado / 100) * PRECO_100G
    print(f"O valor total é R$ {valor_total:.2f}")
else:
    preco_100_desconto = PRECO_100G - 0.50
    valor_total = (peso_comprado / 100) * preco_100_desconto
    print(f"O total é R$ {valor_total:.2f}")

