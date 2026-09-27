print(""" Cursos Disponiveis:
1. SI - Sistemas de Informação
2. ADS - Análise e Desenvolvimento de Sistemas
3. CS - Ciência da Computação 
4. EC - Engenharia da Computação
5. ES - Engenharia de Software
""")
curso = input("Digite a sigla do seu Curso: ").upper()
isento = input("Voce é isento? ").lower()
desconto = int(input("Qual o seu desconto? "))

if curso == "SI":
    valor = 900.00
elif curso == "ADS":
    valor = 750.00
elif curso == "CS":
    valor = 1150.00
elif curso == "EC":
    valor = 1300.00
elif curso == "ES":
    valor = 950.00
else:
    valor = -1

if valor == -1:
    print("Curso não encontrado")
elif isento == "sim":
    print("Valor da mensalidade: R$ 0.00")
else:
    valor_final = valor - (valor * desconto / 100)
    print(f"Valor da mensalidade: R$ {valor_final:.2f}")


