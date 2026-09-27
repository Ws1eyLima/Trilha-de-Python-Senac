dia_atual = int(input("Digite o dia atual com base em numeros de 0 a 6: "))

if dia_atual == 0:
    print("Domingo")
elif dia_atual == 1:
    print("Segunda-Feira")
elif dia_atual == 2:
    print("Terça-Feira")
elif dia_atual == 3:
    print("Quarta-Feira")
elif dia_atual == 4:
    print("Quinta-Feira")
elif dia_atual == 5:
    print("Sexta-Feira")
elif dia_atual == 6:
    print("Sábado")
else:
    print("Dia da Semana Invalido")