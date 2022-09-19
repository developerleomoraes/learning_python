'''Faça um programa que tenha uma lista chamada números e duas funções 
   chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
   e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
   todos os valores pares sorteados pela função anterior.'''

# Importando bibliotecas
from random import randint
from time import sleep

# funções
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for contador in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Fim!')


def soma_pares(lista):
    soma = 0
    for value in lista:
        if value % 2 == 0:
            soma = soma + value
    print(f'Somando os valores pares de {lista}, temos {soma}!')


# Main

números = []
sorteia(números)
soma_pares(números)
