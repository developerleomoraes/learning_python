# Faça um programa que leia um ângulo qualquer e msotre na tela o valor do seno, cosseno e tangente

# Opção com a biblioteca math geral

import math

ângulo   = float(input('Digite o ângulo que você deseja: '))
seno     = math.sin(math.radians(ângulo))
print('O ângulo {} tem o SENO de {:.2f}'. format(ângulo, seno))

cosseno  = math.cos(math.radians(ângulo))
print('O ângulo {} tem o o COSSENO de {:.2f}'.format(ângulo, cosseno))

tangente = math.tan(math.radians(ângulo))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))


# Opção com a biblioteca usando o from math...

'''from math import radians, sin, cos, tan 

ângulo   = float(input('Digite o ângulo que você deseja: '))
seno     = sin(radians(ângulo))
print('O ângulo {} tem o SENO de {:.2f}'. format(ângulo, seno))

cosseno  = cos(radians(ângulo))
print('O ângulo {} tem o o COSSENO de {:.2f}'.format(ângulo, cosseno))

tangente = tan(radians(ângulo))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))'''
