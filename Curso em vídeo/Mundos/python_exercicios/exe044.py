'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS MORAES '))

# Menu
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
      [1] Á vista dinheiro/cheque
      [2] Á vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')

opção = int(input('Qual é a opção: '))

# Verificando a opção de pagamento e imprimindo o resultado devido a cada escolha
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço 
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalParcelas = int(input('Quantas Parcelas? '))
    parcela = total / totalParcelas
    
# Opção Inválida
    print('Sua compra será parcela em {}x de R${:.2f}'.format(totalParcelas, parcela))
else:
    total = 0
    print('Opção inválida de pagamento, tente novamente!')
print('Sua comprar de R${:.2f} vai custar R${:.2f} no final COM JUROS.'. format(preço, total))   


