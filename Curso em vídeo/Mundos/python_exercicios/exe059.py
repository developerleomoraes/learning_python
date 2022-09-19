'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada um'''

from time import sleep

número1 = int(input('Digite o primeiro valor: '))
número2 = int(input('Digite o segundo valor: '))

opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = número1 + número2
        print('A soma entre {} e {} = {}'.format(número1, número2, soma))
        
    elif opção == 2:
        produto = número1 * número2
        print('A multiplicação entre {} e {} = {}'.format(número1, número2, produto))
        
    elif opção == 3:
        if número1 > número2:
            maior = número1
        else:
            maior = número2
        print('O maior número entre {} e {} é {}'.format(número1, número2, maior))
        
    elif opção == 4:
        print('Informe os números novamente ')
        número1 = int(input('Primeiro valor: '))
        número2 = int(input('Segundo valor: '))
        
    elif opção == 5:
        print('Finalizando... ')
        
    else:
        print('Opção Inválida... Tente novamente')
    print('=-=' *10)
    sleep(2)
print('Fim do programa... Volte Sempre!')
