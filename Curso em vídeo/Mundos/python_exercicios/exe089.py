'''Crie um programa que leia nome e duas notas de vários alunos e 
 guarde tudo em uma lista composta. No final, mostre um boletim contendo 
 a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
 
ficha = []

while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    média  = (nota_1 + nota_2) / 2

    ficha.append([nome, [nota_1, nota_2], média])

    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if 'N' in resposta:
        break
    
print('-' * 30)

print(f'{"No.":<4}{"NOME:":<10}{"MÉDIA":>8}')
print('-' * 26)

for indice, aluno in enumerate(ficha):
    print(f'{indice+1:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opção = int(input('Mostrar notas de qual aluno? (999 interompe): '))
    if opção == 999:
        print('Finalizando...')
        break
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
print('<<< VOLTE SEMPRE >>>')

      