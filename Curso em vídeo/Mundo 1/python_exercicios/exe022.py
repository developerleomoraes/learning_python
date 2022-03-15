'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

# Opção 1 mas apenas funciona com 4 digitos
nome = input('Digite seu nome completo: ').strip()

print('Analisando seu nome... ')
#Transformando todas as letras em maiúsculas
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

#Transformando todas as letras em minúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))

#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


