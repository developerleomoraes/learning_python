# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci

print('-=' *12)
print('Sequência de Fibonacci')
print('-=' *12)

n = int(input('Quantos termos você deseja mostrar: '))
n1 = 0 
n2 = 1
print('~' * 20)
print('{} -> {}'.format(n1, n2), end='')
contador = 3
while contador <= n:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    contador = contador + 1
print(' -> Fim')
