print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")
numero_secreto = 45
tentativas = 5
rodada = 1

while(rodada <= tentativas):
    print("Tentativa {} de {}".format(rodada, tentativas))
    numero_str = input("Digite o seu palpite")
    numero = int(numero_str)
    acertou=(numero == numero_secreto)
    maior=(numero > numero_secreto)
    menor=(numero < numero_secreto)


    if acertou:
        print("Você acertou!")
        break
    elif maior:
        print("Você errou, chutou muito pra cima!")
    elif menor:
        print("Você errou, chutou muito pra baixo!")
    rodada= rodada +1
print("Fim")