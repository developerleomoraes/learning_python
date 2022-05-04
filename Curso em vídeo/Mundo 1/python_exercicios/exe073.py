'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

classificação = ('Corinthians', 'Bragantino', 'Atlético-MG', 'Coritiba',
                 'São Paulo', 'Santos', 'Cuiabá', 'Internacional', 'Avaí',
                 'América-Mg', 'Palmeiras', 'Flamengo', 'Chapecoense',
                 'Fluminense', 'Ceará', 'Athletico-PR', 'Atlético-GO',
                 'Juventude', 'Fortaleza')

# Variáveis
contador = 1

print('\n<<<TABELA DE CLASSIFICAÇÃO DO CAMPEONATO BRASILEIRO 2022>>>\n')

#print(f'Lista de times {classificação}')
for t in classificação:
    print(f'{contador} - {t}')
    contador = contador + 1
print('-' * 30)

#Letra A
print(f'Os 5 primeiros são {classificação[0:5]}')
print('-' * 30)

#Letra B
print(f'Os 4 últimos são {classificação[-4:]}')
print('-' * 30)

#Letra C
print(f'Times em ordem alfabética {sorted(classificação)}')
print('-' * 30)

# Letra D
print(f'A Chapecoense está na {classificação.index("Chapecoense")+1}º posição')
