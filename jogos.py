import adivinhacao
import forca

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")


print("(1)Forca e (2) Adivinhação")
jogo = int(input("Digite sua escolha!"))

if jogo == 1:
    print("Jogando forca...")
    forca.jogar_forca()
elif jogo == 2:
    print("Jogando Jogo da Adivinhação...")
    adivinhacao.jogar_adivinhacao()
