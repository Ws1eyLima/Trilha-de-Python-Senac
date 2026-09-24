aluno = input("Digite o nome do aluno: ")
media1 = float(input("Digite a primeira nota: "))
media2 = float(input("Digite a segunda nota: "))
media3 = float(input("Digite a terceira nota: "))

media_final = (media1 + media2 + media3) / 3

print(f"O(A) estudante {aluno} ficou com a media {media_final:.2f}")