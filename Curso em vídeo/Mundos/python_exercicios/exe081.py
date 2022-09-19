''' Crie um programa que vai ler vários números e colocar em uma lista.      
    Depois disso, mostre:                     
    A) Quantos números foram digitados.     
    B) A lista de valores, ordenada de forma decrescente. 
    C) Se o valor 5 foi digitado e está ou não na lista.'''

# Resolução do professor

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    respota = str(input('Quer continuar [S/N]: '))
    if respota in 'Nn':
        break

print('-' * 30)
print(f'Você digitou {len(valores)} elementos!')

valores.sort(reverse = True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não faz parte da lista!')



# Minha resolução
'''# Colocando os números inseridos pleo usuário em um lista
num = []

print('-'* 30)
print('<<< Tratamento de dados >>>')
print('-'* 30)

# Laço
while True:
    num.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if resposta in 'Nn':
        break
    
print('-'* 30)

# Contando qunatos elementos temos na lista
print(f'\nVocê digitou {len(num)} elementos!')

# Printando a lista em ordem decrescente
num.sort(reverse = True)
print(f'Os valores em ordem decrescente são {num}')

# Verificando se o 5 faz parte da lista
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')'''
