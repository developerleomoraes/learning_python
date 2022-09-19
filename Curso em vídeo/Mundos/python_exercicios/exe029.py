'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''

'''Minha tentativa - Falhei na hora de calcular a multa de 7 reais por km acima
from time import sleep
print('---RADAR ELETRÔNICO---')

limite = 80
velocidade = float(input('Lendo a velocidade do carro: '))

print('CALCULADO...')
sleep(3)

if velocidade >= 80:
    print('Você ultrapassou o limite da via {:.1f}km, você será multado!'.format(velocidade - limite))'''
    
# Resolução do professor

velocidade = float(input('Qual é a velocidade atual do carro: '))

if velocidade > 80:
    print('Você foi multado, excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7 
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

print('Tenha um bom dia, dirija com segurança!')

