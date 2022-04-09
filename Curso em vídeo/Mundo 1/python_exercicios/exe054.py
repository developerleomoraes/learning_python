'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

# Importação da biblioteca
from datetime import date

# Definição de variáveis
atual = date.today().year
total_maiores = 0
total_menores = 0

# Aplicação
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu: '.format(pessoas)))
    idade = atual - nascimento

    if idade >= 21:
        total_maiores = total_maiores + 1
    else:
        total_menores = total_maiores + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maiores))
print('Ao todo tivemos {} pessoas menores de idade'.format(total_menores))
