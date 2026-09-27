nota_candidato = float(input("Insira a nota do candidato: "))
nota_de_corte = float(input("Insira a nota de corte: "))
nota_minima = float(input("Insira a nota minima de aprovação: "))

if nota_candidato < nota_de_corte:
    print("Situação do Candidato: Reprovado")
elif nota_candidato >= nota_minima:
    print("Situação do Candidato: Aprovado")
else:
    print("Situação do Candidato: Lista de espera")