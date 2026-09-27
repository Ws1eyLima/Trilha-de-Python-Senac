vendas = 1250.0

if vendas > 1000.0:
    bonus_padrao = 500.0
else:
    bonus_padrao = 100.0

print(f"Com if-else, para vendas de R${vendas:.2f}, o bonus é R$ {bonus_padrao:.2f}")

# ---- Versao 2: Expressao condicional ternaria

Bonus_ternario = 500 if vendas > 1000.0 else 100

print(f"Com ternario, para vendas de R${vendas:.2f}, o bonus é R$ {Bonus_ternario:.2f}")

print("\n Testando com vendas baixas")

vendas = 800.0
Bonus_ternario = 500 if vendas > 1000.0 else 100.0
print(Bonus_ternario)

