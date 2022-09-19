'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

cores = {'limpa':'\033[m', 
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}

print('  Calculando o valor do aumento!  ')
salário = float(input('Digite o valor do salário do funcionário: R$'))

if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)

print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{}'
      .format(cores['azul'], salário, cores['limpa'], 
              cores['amarelo'], novo, cores['limpa']))

