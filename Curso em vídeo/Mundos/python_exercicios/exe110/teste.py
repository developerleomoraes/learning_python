'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe
esse módulo e use algumas dessas funções.
'''

# Importando biblioteca
import moeda

# Main
preço = float(input('Digite um o preço: R$ '))
moeda.resumo(preço, 20, 12)
