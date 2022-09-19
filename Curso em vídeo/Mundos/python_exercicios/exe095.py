'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = []
jogador = {}
partidas = []


while True:
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))

    total = int(input(f'Quantas partidas jogou {jogador["Nome"]}? '))

    for contador in range(0, total):
        partidas.append(int(input(f'   Quantos gols na partida {contador + 1}? ')))
        
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    
    while True:
        resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resposta == 'N':
        break
    
    
print('Cod', end='')  
for index in jogador.keys():
    print(f'{index:<15}', end='')
print()
print('-' * 40)
for key, value in enumerate(time):
    print(f'{key + 1:>3} ', end='')
    for dados in value.values():
        print(f'{str(dados):<15}', end='')
    print()
print('-' * 40)
    
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["Nome"]}:')
        for index, gols in enumerate(time[busca] ['Gols']):
            print(f'    No jogo {index + 1} fez {gols} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')
