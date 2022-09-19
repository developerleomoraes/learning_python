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
