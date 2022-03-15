# Crie um programa que leia um número real qualquer pelo teclado e
# mostrena tela a sua porção inteira

from math import floor

número_float = float(input('Digite um número float que será arredondado para inteiro: '))
número_int = floor(número_float)

print('O número {} arredondado para inteiro fica {}!'.format(número_float, número_int))


# Opção 1 do Guanabara na aula

'''from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'. format(num, trunc(num)))'''


# Opção 2 do Guanabara na aula

'''num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))'''

