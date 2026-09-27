valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao =  input("Digite a operação (Nome ou Número): ")

if operacao == "1" or operacao == "Soma":
    print(f"{valor1} + {valor2} = {valor1 + valor2}")
elif operacao == "2" or operacao == "Subtração":
    print(f"{valor1} - {valor2} = {valor1 - valor2}")
elif operacao == "3" or operacao == "Multiplicação":
    print(f"{valor1} * {valor2} = {valor1 * valor2}")
elif operacao == "4" or operacao == "Divisão":
    print(f"{valor1} / {valor2} = {valor1 / valor2}")
elif operacao == "5" or operacao == "Resto":
    print(f"{valor1} mod {valor2} = {valor1 % valor2}")
elif operacao == "6" or operacao == "Potência":
    print(f"{valor1} ^ {valor2} = {valor1 ** valor2}")
else:
    print("Operação não suportada")

