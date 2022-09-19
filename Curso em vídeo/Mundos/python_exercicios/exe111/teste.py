'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe
esse módulo e use algumas dessas funções.
'''

# Importando biblioteca
from exe111.utilidadescev import moeda

# Main
preço = float(input('Digite um o preço: R$ '))
moeda.resumo(preço, 35, 32)
