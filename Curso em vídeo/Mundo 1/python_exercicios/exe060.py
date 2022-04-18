# Faça um programa que leia um número qualquer e mostre o seu fatorial

# Resolução utilizando a biblioteca Math
'''from math import factorial

num = int(input('Digite um número para calcular seu fatorial: '))
Fatorial = factorial(num)
print('o fatorial de {} é {}!'.format(num, Fatorial))'''

# Resolução tradicional
num = int(input('Digite um número para calcular seu fatorial: '))
contador = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print('{}'.format(fatorial))

