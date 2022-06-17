'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.'''
 
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
     aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5 and aluno['média'] < 7:
     aluno['situação'] = 'Em Recuperação'
else:
     aluno['média'] = 'Aprovado!'
     
for key, value in aluno.items():
    print(f'{key} é igual a {value}')
