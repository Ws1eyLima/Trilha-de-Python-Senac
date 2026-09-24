nome = input("Qual é o seu nome? ")
altura = float(input("Qual é a sua altura em metros? "))
peso = float(input("Qual é o seu peso em kg? "))

calcular_imc = peso / (altura ** 2)

print(f"{nome}, seu IMC é {calcular_imc:.2f}")