quantidade_de_pessoas = int(input("Digite a quantidade de pessoas: "))

PRECO_CARNE = 50.0
PRECO_LINGUICA = 28.0
PRECO_FRANGO = 22.0

CONSUMO_CARNE = 0.3
CONSUMO_LINGUICA = 0.2
CONSUMO_FRANGO = 0.15

if quantidade_de_pessoas <= 0:
    print("Digite um número maior que zero.")
else:
    quantidade_carne = quantidade_de_pessoas * CONSUMO_CARNE
    quantidade_linguica = quantidade_de_pessoas * CONSUMO_LINGUICA
    quantidade_frango = quantidade_de_pessoas * CONSUMO_FRANGO

    custo_carne = quantidade_carne * PRECO_CARNE
    custo_linguica = quantidade_linguica * PRECO_LINGUICA
    custo_frango = quantidade_frango * PRECO_FRANGO

    custo_total = custo_carne + custo_linguica + custo_frango

    print("Quantidades:")
    print(f"Carne: {quantidade_carne:g} kg - Linguiça: {quantidade_linguica:g} kg - Frango: {quantidade_frango:g} kg")
    print()
    print("Custo total:")
    print(f"Carne: R$ {custo_carne:.2f} - Linguiça: R$ {custo_linguica:.2f} - Frango: R$ {custo_frango:.2f}")
    print()
    print(f"Custo total do churrasco: R$ {custo_total:.2f}")
    print(f"Cada pessoa deve contribuir com: R$ {custo_total / quantidade_de_pessoas:.2f}")

