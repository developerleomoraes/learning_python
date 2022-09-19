'''Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

#Criando uma lista que contém uma lista vazia para os pares e outra para os ímpares
num = [[], []]
valor = 0

# Como sabemos a quantidade de repetições, podemos usar um range
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)


print('-' * 30)  
num[0].sort()  # Organizando a lista par em ordem crescente
num[1].sort()  # Organizando a lista ímpar em ordem crescente
print(f'Os valores pares foram {num[0]}')
print(f'Os valores ímpares foram {num[1]}')

