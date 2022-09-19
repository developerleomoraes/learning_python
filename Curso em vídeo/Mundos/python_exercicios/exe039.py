'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

# Bibliotecas
from datetime import date

#Programa

atual = date.today().year

print('<<< ANO DE ALISTAMENTO >>>\n')
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}: '.format(nascimento, idade, atual ))

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('você ainda não tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
    ano_alistamento = atual + saldo
    print('Seu alistamento será em {} ano!'.format(ano_alistamento))
else:
    saldo = idade - 18
    print('Você já deria ter se alistado há {} anos.'.format(saldo))
    ano_alistamento = atual - saldo
    print('Seu alistamento foi em {} ano!'.format(ano_alistamento))
    