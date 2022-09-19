'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

# Minha resolução
'''print('***  Calculando o custo da viagem!   ***\n')

distância = float(input('Qual será distância da viagem: '))
viagem_curta = distância  * 0.5
viagem_longa = distância * 0.45

if distância <= 200:
    print('O valor dessa viagem será de R${:.2f}'.format(viagem_curta))
else:
    print('O valor dessa viagem será R${:.2f}'.format(viagem_longa))'''
    


# Resolução do professor
distância = float(input('qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
    
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço a sua passagem será de R${:.2f}'.format(preço))
