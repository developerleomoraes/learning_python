# Vamos realizar um joge de adivinhação

import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")


    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3)Difícil')

    nivel = int(input('Defina o nível:'))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    
#Conferindo se o random está gerando o número secreto
#print (numero_secreto)


    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
    
    #transformando uma string em int
        chute = int(chute_str)
    
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        print("Você digitou", chute_str)
    

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute) # 20 = 40 - 20
            pontos = pontos - pontos_perdidos
      
    
    print("Fim do Jogo")
2345
if(__name__ == "__main__"):
    jogar()











