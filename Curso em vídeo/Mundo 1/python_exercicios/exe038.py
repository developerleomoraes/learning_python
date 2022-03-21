'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

número_1 = int(input('Digite o primeiro número: '))
número_2 = int(input('Digite o segundo número: '))

if número_1 > número_2:
    print("O PRIMEIRO VALOR é maior!")
elif número_2 > número_1:
    print('O SEGUNDO valor é maior!')
else:
    print('Não existe valor maior, os dois valores são iguais!')
