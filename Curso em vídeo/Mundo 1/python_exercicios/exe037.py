'''Escreva um programa em Python que leia um número inteiro qualquer 
   e peça para o usuário escolher qual será a base de conversão: 
   1 para binário, 2 para octal e 3 para hexadecimal.'''

print('*** CONVERTANDO UM NÚMERO INTEIRO PARA DIFERENTES BASES ***\n')

número = int(input('Digite um número inteiro: '))

print('''\nEscolha uma das bases para conversão:\n
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opção = int(input("Sua opção: "))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(número, oct(número)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(número, hex(número)[2:]))
else:
    print('Opção Inválida, tente novamente!')
