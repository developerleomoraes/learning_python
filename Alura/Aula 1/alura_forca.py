# Vamos realizar um joge da forca

import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo da Forca!")
    print("*********************************")
    
    lista_palavras = []
    
    with open("palavras.txt") as arquivo:
        for item in arquivo:
            item = item.strip()
            lista_palavras.append(item)
            

    #arquivo = open('palavras.txt', 'r')
       
    
    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero].upper()
    
    
    palavra_secreta =  'maça'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    
    
    enforcou = False
    acertou  = False
    erros    = 0
    
    print(letras_acertadas)
    
    #Enquanto não se enforcou e não acertou a palavra secreta o jogo irá continuar
    while(not enforcou and not acertou):
        
        chute = input('Qual letra?')
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou  = erros = 6
        acertou   = '_' not in letras_acertadas
        print(letras_acertadas)
        
        if(acertou):
            print('Você ganhou!')
        else:
            print('Você perdeu!')
        
        
        print(letras_acertadas)
    
    print('Fim de jogo')
    
if(__name__ == "__main__"):
    jogar()


