PERCENTUAL_RESERVA = 0.30

meta_pessoal = input("Digite o que deseja comprar: ")
valor_meta = float(input("Digite o valor da meta: "))
salario = float(input("Digite o valor do seu salário: "))
despesas = float(input("Digite o valor das suas despesas: "))

saldo = round(salario - despesas, 2)
reserva_fixa = round(saldo * PERCENTUAL_RESERVA, 2)
valor_disponivel = round(saldo - reserva_fixa, 2)

print(f"Meta: {meta_pessoal} (R$ {valor_meta:.2f})")
print(f"Salário: R$ {salario:.2f} - Despesas: R$ {despesas:.2f}")
print()

if valor_disponivel <= 0:
    print(f"Saldo após despesas: R$ {saldo:.2f}")
    print("Não sobra valor para a meta. Reduza as despesas ou aumente a renda.")
else:
    prazo_meses = valor_meta / valor_disponivel

    print(f"Saldo após despesas: R$ {saldo:.2f}")
    print(f"Reserva fixa (30%): R$ {reserva_fixa:.2f}")
    print(f"Valor disponível para a meta: R$ {valor_disponivel:.2f} por mês")
    print(f"Prazo estimado para atingir a meta: {prazo_meses:.2f} meses")