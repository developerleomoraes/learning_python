'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

# Importando bibliotecas
from time import sleep


# Funções
def maior(*números):
    contador = 0
    maior    = 0
    print('-' * 30)
    
    print('Analisando os valores passados...')
    for valor in números:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador = contador + 1
        
    print(f'\nForam informado {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}!')
        

# Main
maior(2, 9, 4, 7, 3 ,7, 4, 5, 8, 3)
maior(2, 6 ,4)
maior(1, 4)
maior(6)
maior()
