'''Crie um programa que leia nome, sexo e idade de várias pessoas,
   guardando os dados de cada pessoa em um dicionário e todos os dicionários
   em uma lista. No final, mostre:
        A) Quantas pessoas foram cadastradas
        B) A média de idade
        C) Uma lista com as mulheres
        D) Uma lista de pessoas com idade acima da média'''
      
      
# Realizando a etapa que pega os dados     
        
pessoa = {}
galera = []
soma = 0
média = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))

    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F/NB]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'M F NB':
            break
        print('ERRO! Por favor digite apenas M, F ou NB')
        
    pessoa['Idade'] = int(input('Idade: '))
    soma = soma + pessoa['Idade']
    
    galera.append(pessoa.copy())
    
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while True:
        if resposta in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N!')
    if resposta == 'N':
        break


print('-' * 30)

# Letra A
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas. ')

# Letra B
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')

# Letra C
print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in galera:
    if pessoa['Sexo'] == 'F':
        print(f'{pessoa["Nome"]} ', end='')
print()

# Letra D
print(f'D) Lista de pessoas que estão acima da média da idade: ', end='')
for pessoa in galera:
    if pessoa['Idade'] >= média:
        print('         ', end='')
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<< ENCERRANDO >> ')
