'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe
esse módulo e use algumas dessas funções.
'''

# Importando biblioteca
import moeda

# Main
preço = float(input('Digite um o preço: R$ '))
print(f'A metade do {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {(moeda.dobro(preço, True))}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço, 13, True)}')
