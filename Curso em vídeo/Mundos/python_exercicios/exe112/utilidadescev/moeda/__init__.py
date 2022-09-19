'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe
esse módulo e use algumas dessas funções.
'''

# criando funções

def aumentar(preço=0, taxa = 0, formato=False):
    res = preço + (preço * taxa) / 100
    if formato is False:
        return res
    else:
        return moeda(res)

def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa) / 100
    if formato is False:
        return res
    else:
         return moeda(res)

def dobro(preço = 0, formato=False):
    res = preço * 2
    if formato is False:
        return res
    else:
        return moeda(res)

def metade(preço = 0, formato=False):
    res = preço / 2
    if formato is False:
        return res
    else:
        return moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxa_aum=10, taxa_red=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(preço, taxa_aum, True)}')
    print(f'{taxa_red}% de redução: \t{diminuir(preço, taxa_red, True)}')
    print('-' * 30)
