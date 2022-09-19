# Um professor quer sotear um dos seus quatros alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

# Opção com a biblioteca toda

import random

nome_1 = input("Primeiro aluno: ")
nome_2 = input('Segundo aluno: ')
nome_3 = input('Terceiro aluno: ')
nome_4 = input('Quarto aluno: ')

# Organizando todos os alunos em uma lista
lista = [nome_1, nome_2, nome_3, nome_4]

# Usando a biblioteca random com a função choice para escolher um aluno
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))

'''Opção com imporante apenas o choice

from random import choice

nome_1 = input("Primeiro aluno: ")
nome_2 = input('Segundo aluno: ')
nome_3 = input('Terceiro aluno: ')
nome_4 = input('Quarto aluno: ')

# Organizando todos os alunos em uma lista
lista = [nome_1, nome_2, nome_3, nome_4]

# Usando a biblioteca random com a função choice para escolher um aluno
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))'''
