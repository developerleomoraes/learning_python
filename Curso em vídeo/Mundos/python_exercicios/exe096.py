'''Faça um programa que tenha uma função chamada área(), que receba as 
 dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
 
# Funções
def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} = {a}m²')


# Main
print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento  = float(input('COMPRIMENTO (m): '))

área(largura, comprimento)

