semaforo = str(input("Digite a cor atual do semaforo: "))

if semaforo == "Vermelho":
    print("Espere")
elif semaforo == "Verde":
    print("Atravesse")
elif semaforo == "Roxo":
    print("Farol Inoperante")
else:
    print("Cor inexistente, insira uma cor valida")

