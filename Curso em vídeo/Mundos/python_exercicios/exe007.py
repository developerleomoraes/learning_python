# Desenvolvendo um programa que lê as duas notas de um aluno e mostre sua média

print('Calculando a média do aluno(a)\n')

nome = input('Digite o nome do aluno(a): ')

nota1 = float(input('Digite a primeira nota do(a) aluno(a): '))
nota2 = float(input('Digite a segunda nota do(a) aluno(a): '))

media = (nota1 + nota2) / 2

print('A média de {}, é {}!'.format(nome, media))

