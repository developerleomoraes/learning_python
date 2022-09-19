'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.'''

# Importando o gerador de números
from random import randint

# Variável global
vitória = 0

# Jogo em si 
while True:
    print('-=' * 30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 30)
    
    # O jogador digita o número que deseja jogar
    jogador = int(input('Diga um valor: '))
    
    # O computador gera um valor aleatório a partir da randint entre 0 e 10
    computador = randint(0,11)
    total = jogador + computador
    
    # É craido o 'Tipo' um str vazia
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    if total % 2 == 0:
        print('DEU PAR!')
    else:
        print('DEU ÍMPAR')
        
    # Se for Par
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitória = vitória + 1
        else:
            print('Você PERDEU!')
            break
        
    # Se for Ímpar
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU!')
            vitória = vitória + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitória} vezes!')
        
