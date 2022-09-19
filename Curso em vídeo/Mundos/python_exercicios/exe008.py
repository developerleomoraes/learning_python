# Escrevendo um código que leia o valor em metros e exiba o valor em cm

from typing import ChainMap


print('    Programa que passa metros para centimetros    ')

medida = float(input('Digite uma distância em metros: '))
cm      = medida * 100
mm      = medida * 1000

print('A media de {} corresponde a {:.0f}cm e {:.0f}mm!'.format(medida, cm, mm))

