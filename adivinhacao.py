print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")
numero_secreto = 45

numero_str = input("Digite o seu palpite")
numero = int(numero_str)
acertou=(numero == numero_secreto)
maior=(numero > numero_secreto)
menor=(numero < numero_secreto)


if acertou:
    print("Você acertou!")
elif maior:
    print("Você errou, chutou muito pra cima!")
elif menor:
    print("Você errou, chutou muito pra baixo!")

print("Fim")