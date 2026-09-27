qtd_inteiras = int(input("Quantidade de Ingressos inteiros: "))
qtd_meias = int(input("Quantidade de Meias-entradas: "))
dia = input("Dia da semana: ").lower()
nacional = input("O filme é naciona? (sim/não): ").lower()

if nacional == "sim":
    preco_inteira = 5.00
    preco_meia = 5.00
elif dia == "quarta-feira":
    preco_inteira = 14.50
    preco_meia = 14.50
else:
    preco_inteira = 28.50
    preco_meia = 14.25

total = (qtd_inteiras * preco_inteira) + (qtd_meias * preco_meia)
print(f"Total à pagar: R$ {total:.2f}")