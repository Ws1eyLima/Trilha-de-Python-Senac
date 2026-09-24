acai_p = int(input("Quantos copos de açai P você deseja? "))
acai_m = int(input("Quantos copos de açai M você deseja? "))
acai_g = int(input("Quantos copos de açai G você deseja? "))
desconto = float(input("Digite o valor do desconto (em %): "))

VALOR_P = 13.50
VALOR_M = 15.00
VALOR_G = 17.50

print("Seu pedido foi registrado")
print(f"- Açai P: {acai_p}")
print(f"- Açai M: {acai_m}")
print(f"- Açai G: {acai_g}")

print(f"Desconto de {desconto:.2f}% aplicado")
print(f"Total R${(acai_p * VALOR_P + acai_m * VALOR_M + acai_g * VALOR_G) * (1 - desconto / 100):.2f}")

