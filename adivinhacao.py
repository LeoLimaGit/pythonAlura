import random

print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")
numero_secreto = (random.randrange(1, 101))
tentativas = 5

for rodada in range(1, tentativas +1 ):
    print("Tentativa {} de {}".format(rodada, tentativas))
    numero_str = input("Digite o seu palpite,de 0 a 100: ")
    numero = int(numero_str)
    print("Você digitou: ", numero)


    acertou=(numero == numero_secreto)
    maior=(numero > numero_secreto)
    menor=(numero < numero_secreto)

    if numero < 0 or numero > 100:
        print("Digite um valor entre 0 e 100")
        continue

    if acertou:
        print("Você acertou!")
        break
    elif maior:
        print("Você errou, chutou muito pra cima!")
    elif menor:
        print("Você errou, chutou muito pra baixo!")

print("Fim")