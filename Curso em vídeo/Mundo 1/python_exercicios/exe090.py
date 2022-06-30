'''Faça um programa que leia Nome e Média de um aluno, guardando também a Situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.'''
 
aluno = {}
aluno['Nome']  = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
     aluno['Situação'] = 'Aprovado!'
elif aluno['Média'] >= 5 and aluno['Média'] < 7:
     aluno['Situação'] = 'Recuperação'
else:
     aluno['Situação'] = 'Reprovado!'
     
print('-' * 30)

for key, value in aluno.items():
     print(f'- {key} é igual a {value}')
