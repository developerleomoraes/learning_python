'''Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

contador = soma = 0

while True:
    num = int(input('Digite um número [999 é a condição de parada]: '))
    if num == 999:
        break
    contador = contador + 1
    soma = soma + num
print(f'Foram digitados {contador} números e soma entre eles é {soma}!')
