nome = input("Qual é o seu nome? ")
livros = str(input("Qual livro você está lendo? "))
quantidade_paginas = int(input("Quantas páginas tem o livro? "))
tempo_por_pagina = float(input("Quanto tempo você leva para ler uma página (em segundos)? "))

tempo_total = quantidade_paginas * tempo_por_pagina
conversao_horas = tempo_total / 3600

print(f"{nome}, você finalizara o livro '{livros}' em aproximadamente {conversao_horas:.2f} horas.")