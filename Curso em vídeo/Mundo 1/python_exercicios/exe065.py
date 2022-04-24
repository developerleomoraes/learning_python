'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

# Variáveis
resposta = 'S'
média = soma = quantidade = maior = menor = 0

# Estrutura do programa
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
média = soma / quantidade
print('Você digitou {} números e a média foi {}!'.format(quantidade, média))
print('O maior valor foi {} e o menor foi {}!'.format(maior, menor))
