'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''

# Importando bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

# Definindo o dicionário do jogo
jogo = { 'Jogador_1': randint(1, 6),
         'Jogador_2': randint(1, 6),
         'Jogador_3': randint(1, 6),
         'Jogador_4': randint(1, 6)}

# Criando uma lista para rankear os jogadores
ranking = []

# Sortenado os valores conforme key e value
print('Valores Sorteados:')
for key, value in jogo.items():
    print(f'A {key} tirou {value} no dado!')
    sleep(1)

# Usando a função itemgetter para ordenar as jogadas e depois
# usando o reverse=True para colocar na decrescente
ranking = sorted(jogo.items(),key=itemgetter(1), reverse = True)
print('-' * 30)

print('  == RANKING DOS JOGADORES ==  ')

# Printnado o ranking conforme organizado na lista
for index, value in enumerate(ranking):
    print(f'   {index + 1}º lugar: {value[0]} com {value[1]}')
    sleep(1)
