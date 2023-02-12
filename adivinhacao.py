print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")
numero_secreto = 45

numero_str = input("Digite o seu palpite")
numero = int(numero_str)


if numero == numero_secreto:
    print("Você acertou!")
else:
    if numero>numero_secreto:
        print("Você chutou muito pra cima!")
    elif numero<numero_secreto:
        print("Você chutou muito pra baixo!")
