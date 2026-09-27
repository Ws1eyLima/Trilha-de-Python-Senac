nota1 = float(input("Insira a Primeira nota: "))
nota2 = float(input("Insira a Segunda nota: "))
nota3 = float(input("Insira a Terceira nota: "))
faltas = int(input("Insira a quantidade de Faltas: "))

media = (nota1 + nota2 + nota3) / 3

if faltas > 4:
    print(f"Média: {media}")
    print("Situação: Reprovado por falta")
elif media == 0:
    print(f"Média: {media}")
    print("Situação: Desistente")
elif 8 <= media <= 10:
    print(f"Média: {media}")
    print("Situação: Aprovado com sucesso")
elif 6 <= media <= 8:
    print(f"Média: {media}")
    print("Situação: Aprovado")
else:
    print(f"Média: {media}")
    print("Situação: Recuperação")