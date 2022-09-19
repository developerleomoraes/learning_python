#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Opção 1
'''numero = int(input('Digite um número: ')).strip
n = str(numero)
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena:  {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar:  {}'.format(n[0]))'''

# Opção 2 

numero = int(input('Informe um número: '))

unidade = numero // 1 % 10
dezena  = numero // 10 % 10
centena = numero // 100 % 10
milhar  = numero // 1000 % 10

print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena:  {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar:  {}'.format(milhar))
