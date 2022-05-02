'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total_compra = produtos_acima1000 = mais_barato = contador = 0
nome_barato = ' '
while True:
    print('-' * 20)
    print('<<< LOJA SUPER BARATÃO >>>')
    print('-' * 20)
    
    produto  = str(input('Qual o nome do produto: '))
    preço    = float(input('Preço: R$ '))
    contador = contador + 1
  
    total_compra = total_compra + preço
    if preço > 1000:
        produtos_acima1000 = produtos_acima1000 + 1
    if contador == 1:
        mais_barato = preço
        nome_barato = produto
    else:
        if preço < mais_barato:
            mais_barato = preço
            nome_barato = produto
        
    escolha = ' '
    while escolha not in 'SN':
         escolha = str(input('Qual a sua escolha: [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
print('{:^40}'.format('\nFIM DO PROGRAMA'))
print(f'O valor total da compra é: R${total_compra:.2f}')
print(f'Temos {produtos_acima1000} que custa mais de R$1.000,00')
print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato:.2f}')
