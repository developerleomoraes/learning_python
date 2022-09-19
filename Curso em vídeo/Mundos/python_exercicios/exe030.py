# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

'''Minha resolução
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')'''
    

# Resolução do professor

número = int(input('Me diga um número qualquer: '))

resultado = número % 2
if resultado == 0:
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é ÍMPAR!'.format(número))


    