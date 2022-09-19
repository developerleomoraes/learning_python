'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

tot18 = total_homens = tot_mulheres_20 = 0


while True:
    print('-' * 20)
    print('<<< CADASTRE UMA PESSOA >>>\n')
    print('-' * 20)
    
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo  = str(input('[M/F/NB]: ')).strip().upper()[0]
    print('-' * 20)
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        total_homens = total_homens + 1
    if sexo == 'F' and idade < 20:
        tot_mulheres_20 = tot_mulheres_20 + 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar: [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
        
        
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {total_homens} homens cadastrados!')
print(f'E temos {tot_mulheres_20} de mulheres com menos de 20 anos!')

    