import random
def jogar_forca():


    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")



    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

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
        print(letras_acertadas)
    else:
        print("Você perdeu")
    print("Fim do jogo")

if __name__ == "__main__":
    jogar_forca()