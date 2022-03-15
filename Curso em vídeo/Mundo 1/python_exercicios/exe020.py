# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de tabalhos dos alunos. 
# Faça um programa que leia o nome o nome dos quatro alunos e mostre a ordem sorteada.

# Opção 1, usando a biblioteca toda
import random

# Inserindo o nome dos alunos
nome_1 = input('Primeiro aluno: ')
nome_2 = input('Segundo aluno: ')
nome_3 = input('Terceiro aluno: ')
nome_4 = input('Quarto aluno: ')

# Colocando o nome dos alunos dentro de uma lista
lista = [nome_1, nome_2, nome_3, nome_4]

# Embaralhando os nomes
random.shuffle(lista)

# Apresentando o resultado do shuffle
print('A ordem de apresentação será ')
print(lista)

# Opção 2 importando apenas o shuffle

'''from random import shuffle

# Inserindo o nome dos alunos
nome_1 = input('Primeiro aluno: ')
nome_2 = input('Segundo aluno: ')
nome_3 = input('Terceiro aluno: ')
nome_4 = input('Quarto aluno: ')

# Colocando o nome dos alunos dentro de uma lista
lista = [nome_1, nome_2, nome_3, nome_4]

# Embaralhando os nomes
shuffle(lista)

# Apresentando o resultado do shuffle
print('A ordem de apresentação será ')
print(lista)'''
