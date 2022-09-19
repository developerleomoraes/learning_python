'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
   peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
   O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

'''Opção feita por mim
import random

number = random.randrange(0, 5)

chute = int(input('Digite o seu chute de qual número entre 0 e 5 o computador pensou: '))

if chute == number:
    print('Você acertou, parabéns!')
else:
    print('Você errou, o computador venceu!')

print('O computador pensou no número {}'.format(number))
print('--FIM--')'''

# Opção feita pelo professor

from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))
