import forca
import adivinhacao

def escolhe_jogo():
            print("*******************************")
            print("Escolha o seu Jogo!")
            print("*******************************")

            print("(1) Forca (2) Adivinhação")
            jogo = int(input("Qual Jogo?"))

            if(jogo == 1):
                forca.jogar_forca()
            elif(jogo == 2):
                adivinhacao.jogar_advinhacao()


if(__name__ == "__main__"):
    escolhe_jogo()