'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe
esse módulo e use algumas dessas funções.
'''

# Importando biblioteca
import moeda

# Main
preço = float(input('Digite um o preço: R$ '))
print(f'A metade do R${preço} é R${moeda.metade(preço)}')
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preço, 10)}')
