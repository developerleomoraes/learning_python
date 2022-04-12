'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos'''

# Declarando as variáveis
soma_idade = 0
média = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0

# Emplementando a solução
for pessoas in range(1, 5):
    print('\n----- {}ª Pessoa -----'.format(pessoas))
    nome  = input("Nome: ").strip()
    idade = int(input('Idade: '))
    sexo  = input('Sexo [M/F/NB]: ').strip()
    
    soma_idade = soma_idade + idade
    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Fm' and idade < 20:
        tot_mulher_20 = tot_mulher_20 + 1
    
# Printando o resultado
média = soma_idade / 4
print('A média de idade do grupo é {} anos!'.format(média))
print('O homem mais velho tem {} anos e se chama {}!'.format(maior_idade_homem, nome_velho))
print('São {} mulheres com menos de 20 anos'.format(tot_mulher_20))

