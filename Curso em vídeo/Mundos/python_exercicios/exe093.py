'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
partidas = []

jogador['Nome'] = str(input('Nome do Jogador: '))

total = int(input(f'Quantas partidas jogou {jogador["Nome"]}? '))

for contador in range(0, total):
    partidas.append(int(input(f'   Quantos gols na partida {contador + 1}? ')))
    
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print('-' * 30)
print(jogador)

print('-' * 30)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')
    
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')   
for index, value in enumerate(jogador['Gols']):
    print(f'          => Na partida {index + 1}, fez {value} gols.')
print(f'foi um total de {jogador["Total"]} gols!')
