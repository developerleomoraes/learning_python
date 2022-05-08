'''Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.'''

# Tupla
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.25,
            'Compasso', 9.99,
            'Mochila', 120.75,
            'Caneta', 1.75,
            'Lápis', 1.80,
            'Livro', 34.75,)

#Formatação dos dados
print('-' * 40)
print(f'{"<<<LISTAGEM DE PREÇOS>>>":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0: 
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
