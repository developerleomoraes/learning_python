'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''


num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),)
print(f'Você digitou os valores {num}')

print(f'O número 9 aparece {num.count(9)} vezes!')

if 3 in num:
   print(f'O valor três apareceu na {num.index(3)+1}ª posição!') 
else:
    print(f'O valor 3 não digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')

for número in num:
    if número % 2 == 0:
        print(número, end=' ')
    