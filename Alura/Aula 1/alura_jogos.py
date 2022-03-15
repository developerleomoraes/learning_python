# Vamos escolher o jogo

import alura_forca
import alura_adivinhação

def escolhe_jogo():

    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual jogo?')) 


    if(jogo == 1):
        print('Jogando Forca')
        alura_forca.jogar()
    elif(jogo == 2):
        print('Jogando adivinhação')
        alura_adivinhação.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()

