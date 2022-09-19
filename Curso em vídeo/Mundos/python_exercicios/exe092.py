'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''

# Importando biblioteca
from datetime import datetime

dados = {}

# Inserindo as keys e values dentro do dicionário
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

# Se o funcionário tiver carteira de trabalho entra nesse if
if dados['CTPS'] != 0:
    dados['Contratação']   = int(input('Ano de contratação: '))
    dados['Salário']       = float(input('Digite o salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

print('-' * 30)

# Printando formatado
for key, value in dados.items():
    print(f'{key} tem o valor {value}')
