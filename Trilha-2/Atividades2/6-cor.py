cor_primaria1 = input("Coloque a primeira opçao:")
cor_primaria2 = input("Coloque a segunda opçao:")

if (cor_primaria1 == "Vermelho" and cor_primaria2 == "Azul") or (cor_primaria1 == "Azul" and cor_primaria2 == "Vermelho"):
    print("A combinação resulta em: Roxo")
else:
    print("Apenas cores primárias são aceitas.")