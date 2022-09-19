# Realizando um programa, lê o comprimento de um cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcula e msotra o comprimento da hiponetusa


# Opção importando da biblioteca math

from math import hypot

cateto_oposto    = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa       = hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))



# Opção sem importar biblioteca nenhuma

'''cateto_oposto    = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa       = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

