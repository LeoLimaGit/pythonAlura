
def jogar_forca():


    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")
    palavra_secreta= "python".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0
    while(not enforcou and not acertou):
        chute = input("Qual letra? :")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Você errou! Faltam {} tentaivas".format(6- erros))
        if erros == 6:
            break
        if ("_" not in letras_acertadas):
            break

        print(letras_acertadas)
    if ("_" not in letras_acertadas):
        print("Você ganhou!")
    else:
        print("Você perdeu")
    print("Fim do jogo")

if __name__ == "__main__":
    jogar_forca()