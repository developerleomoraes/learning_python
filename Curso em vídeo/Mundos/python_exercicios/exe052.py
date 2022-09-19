# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite o número: '))

total = 0
for contador in range(1, num + 1):
    if num % contador == 0:
        print('\033[34m', end='')
        total = total + 1
    else:
        print('\033[m', end='')
    print('{} '.format(contador), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))

if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO') 
