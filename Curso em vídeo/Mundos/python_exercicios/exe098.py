''' Faça um programa que tenha uma função chamada contador(),
    que receba três parâmetros: início, fim e passo. Seu programa
    tem que realizar três contagens através da função criada:                                                                                                                                                                         
    a) de 1 até 10, de 1 em 1                                                                                                                                           
    b) de 10 até 0, de 2 em 2                                                                                                                                          
    c) uma contagem personalizada'''

# Importando Bibliotecas
from time import sleep


# funções
def contador(início, fim , passo):
    
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1
        
    print('-' * 30)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(2)
    
    if início <= fim:
        contador = início
        while contador <= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador = contador + passo
        print('Fim!')
    else:
        contador = início
        while contador >= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador = contador - passo
        print('Fim')
    


# Main
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
























































'''from time import sleep

# Funções

def linha():
    print('-' * 20)


def contador(início, fim, passo):
    print('-' * 20)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    
    sleep(2)
    if início < fim:
        contador = início
        while contador <= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador = contador + passo
        print('Fim!')
    else:
        contador = início
        while contador >= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador = contador - passo
        print('Fim!')
    print('-' * 20)



# Main

linha()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim    = int(input('Fim:    '))
passo  = int(input('Passo:  '))
contador(início, fim, passo)'''
