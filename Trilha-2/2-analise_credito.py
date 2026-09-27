# Regras de negocio
RENDA_MINIMA = 4000.0
SCORE_MINIMO = 600

print("Bem-vindo ao sistema de análise de crédito!")
print(f"Regra de negócio: Renda mínima de {RENDA_MINIMA} e Score mínimo de {SCORE_MINIMO}.")

# Cliente 1: Carlos 
renda_carlos = 5500.0
score_carlos = 720

# Cliente 2: Ana
renda_ana = 6000.0
score_ana = 550

# Cliente 3
renda_joao = 3500.0
score_joao = 900

aprovado_carlos = (renda_carlos >= RENDA_MINIMA) and (score_carlos >= SCORE_MINIMO)
print(f"Analise de crédito para Carlos: {'Aprovado' if aprovado_carlos else 'Reprovado'}")

aprovado_ana = (renda_ana >= RENDA_MINIMA) and (score_ana >= SCORE_MINIMO)
print(f"Analise de crédito para Ana: {'Aprovado' if aprovado_ana else 'Reprovado'}")

aprovado_joao = (renda_joao >= RENDA_MINIMA) or (score_joao >= SCORE_MINIMO)
print(f"Analise de crédito para João: {'Aprovado' if aprovado_joao else 'Reprovado'}")
